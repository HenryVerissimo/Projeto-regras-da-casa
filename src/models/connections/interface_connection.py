from abc import ABC, abstractmethod


class InterfaceConnection(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass
