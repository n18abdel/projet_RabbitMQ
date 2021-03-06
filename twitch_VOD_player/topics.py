from typing import Union

from pika.adapters.blocking_connection import BlockingChannel

from amqp import publish


def json(channel: BlockingChannel, chat: Union[str, bytes]) -> None:
    publish(channel, "json", chat)


def seek(channel: BlockingChannel, pos: str) -> None:
    publish(channel, routing_key="sync.seek", body=pos)


def play(channel: BlockingChannel, pos: str) -> None:
    publish(channel, routing_key="sync.play", body=pos)


def pause(channel: BlockingChannel, pos: str) -> None:
    publish(channel, routing_key="sync.pause", body=pos)


def timer(channel: BlockingChannel, pos: str) -> None:
    publish(channel, routing_key="sync.timer", body=pos)


def speed(channel: BlockingChannel, speed: float) -> None:
    publish(channel, routing_key="sync.speed", body=str(speed))


def chatExit(channel: BlockingChannel) -> None:
    publish(channel, routing_key="exit", body="")
