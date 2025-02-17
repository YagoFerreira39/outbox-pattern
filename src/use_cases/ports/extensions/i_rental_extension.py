from abc import ABC, abstractmethod

from src.domain.models.rental_event_message_model import RentalEventMessageModel
from src.domain.models.rental_event_model import RentalEventModel
from src.domain.models.rental_model import RentalModel
from src.use_cases.data_types.dtos.rental_dto import RentalDto


class IRentalExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_database_result_to_model(result: dict) -> RentalModel:
        pass

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: RentalModel) -> RentalDto:
        pass

    @staticmethod
    @abstractmethod
    def create_rental_event_model(model: RentalModel) -> RentalEventModel:
        pass

    @staticmethod
    @abstractmethod
    def from_database_result_to_event_model_list(
        result_list: list[dict],
    ) -> list[RentalEventModel]:
        pass

    @staticmethod
    @abstractmethod
    def create_rental_event_message_model(
        rental_event_model: RentalEventModel,
    ) -> RentalEventMessageModel:
        pass
