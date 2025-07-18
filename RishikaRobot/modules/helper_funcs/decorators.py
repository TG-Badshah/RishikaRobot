from typing import List, Optional, Union

from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
)
from telegram.ext.filters import MessageFilter

from RishikaRobot import LOGGER
from RishikaRobot import dispatcher as n
from RishikaRobot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler


class AvishaTelegramHandler:
    def __init__(self, n):
        self._dispatcher = n

    def command(
        self,
        command: str,
        filters: Optional[MessageFilter] = None,
        admin_ok: bool = False,
        pass_args: bool = False,
        pass_chat_data: bool = False,
        run_async: bool = True,
        can_disable: bool = True,
        group: Optional[Union[int, str]] = 40,
    ):
        def _command(func):
            try:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                        ),
                        group,
                    )
                else:
                    self._dispatcher.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                        ),
                        group,
                    )
                LOGGER.debug(
                    f"[AvishaCmd] Loaded handler {command} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                else:
                    self._dispatcher.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                LOGGER.debug(
                    f"[AvishaCMd] Loaded handler {command} for function {func.__name__}"
                )

            return func

        return _command

    def message(
        self,
        pattern: Optional[str] = None,
        can_disable: bool = True,
        run_async: bool = True,
        group: Optional[Union[int, str]] = 60,
        friendly=None,
    ):
        def _message(func):
            try:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        ),
                        group,
                    )
                else:
                    self._dispatcher.add_handler(
                        MessageHandler(pattern, func, run_async=run_async), group
                    )
                LOGGER.debug(
                    f"[AvishaMsg] Loaded filter pattern {pattern} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._dispatcher.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        )
                    )
                else:
                    self._dispatcher.add_handler(
                        MessageHandler(pattern, func, run_async=run_async)
                    )
                LOGGER.debug(
                    f"[RishikaRobot-Msg] Loaded filter pattern {pattern} for function {func.__name__}"
                )

            return func

        return _message

    def callbackquery(self, pattern: str = None, run_async: bool = True):
        def _callbackquery(func):
            self._dispatcher.add_handler(
                CallbackQueryHandler(
                    pattern=pattern, callback=func, run_async=run_async
                )
            )
            LOGGER.debug(
                f"[RishikaRobot-Callback] Loaded callbackquery handler with pattern {pattern} for function {func.__name__}"
            )
            return func

        return _callbackquery

    def inlinequery(
        self,
        pattern: Optional[str] = None,
        run_async: bool = True,
        pass_user_data: bool = True,
        pass_chat_data: bool = True,
        chat_types: List[str] = None,
    ):
        def _inlinequery(func):
            self._dispatcher.add_handler(
                InlineQueryHandler(
                    pattern=pattern,
                    callback=func,
                    run_async=run_async,
                    pass_user_data=pass_user_data,
                    pass_chat_data=pass_chat_data,
                    chat_types=chat_types,
                )
            )
            LOGGER.debug(
                f"[AvishaINLINE] Loaded inlinequery handler with pattern {pattern} for function {func.__name__} | PASSES "
                f"USER DATA: {pass_user_data} | PASSES CHAT DATA: {pass_chat_data} | CHAT TYPES: {chat_types}"
            )
            return func

        return _inlinequery


Avishacmd = AvishaTelegramHandler(n).command
Avishamsg = AvishaTelegramHandler(n).message
Avishacallback = AvishaTelegramHandler(n).callbackquery
Avishainline = AvishaTelegramHandler(n).inlinequery
              
