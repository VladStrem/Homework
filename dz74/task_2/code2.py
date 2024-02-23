from abc import ABC, abstractmethod


class VideoChannel(ABC):
    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber) -> None:
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber) -> None:
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, video) -> None:
        for subscriber in self._subscribers:
            subscriber.update(video)

    @abstractmethod
    def publish_video(self, video_title: str) -> None:
        pass


class Subscriber(ABC):
    @abstractmethod
    def update(self, video) -> None:
        pass


class Video:
    def __init__(self, title: str):
        self.title = title


class ConcreteVideoChannel(VideoChannel):
    def __init__(self, channel_name: str):
        super().__init__()
        self._channel_name = channel_name

    def publish_video(self, video_title: str) -> None:
        new_video = Video(video_title)
        print(f"New video published on {self._channel_name}: {new_video.title}")
        self.notify_subscribers(new_video)


class ConcreteSubscriber(Subscriber):
    def __init__(self, subscriber_name: str):
        self._subscriber_name = subscriber_name

    def update(self, video) -> None:
        print(f"Subscriber {self._subscriber_name} received a notification about the new video: {video.title}")


if __name__ == "__main__":
    channel = ConcreteVideoChannel("Awesome Channel")

    subscriber1 = ConcreteSubscriber("User1")
    subscriber2 = ConcreteSubscriber("User2")

    channel.add_subscriber(subscriber1)
    channel.add_subscriber(subscriber2)

    channel.publish_video("Introduction to Python Programming")
