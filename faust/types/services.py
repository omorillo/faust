import abc
import asyncio

__all__ = ['ServiceT']


class ServiceT(metaclass=abc.ABCMeta):
    """Abstract type for an asynchronous service that can be started/stopped.

    See Also:
        :class:`faust.utils.services.Service`.
    """

    shutdown_timeout: float
    wait_for_shutdown = False
    loop: asyncio.AbstractEventLoop = None

    @abc.abstractmethod
    async def __aenter__(self) -> 'ServiceT':
        ...

    @abc.abstractmethod
    async def __aexit__(*exc_info) -> None:
        ...

    @abc.abstractmethod
    def on_init(self) -> None:
        ...

    @abc.abstractmethod
    async def on_start(self) -> None:
        ...

    @abc.abstractmethod
    async def on_stop(self) -> None:
        ...

    @abc.abstractmethod
    async def on_shutdown(self) -> None:
        ...

    @abc.abstractmethod
    async def start(self) -> None:
        ...

    @abc.abstractmethod
    async def maybe_start(self) -> None:
        ...

    @abc.abstractmethod
    async def stop(self) -> None:
        ...

    @abc.abstractmethod
    def set_shutdown(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def started(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def should_stop(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def state(self) -> str:
        ...
