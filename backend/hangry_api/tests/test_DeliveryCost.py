from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel
import pytest

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

@pytest.mark.parametrize('quantity, delivery_distance', [
  (0, 0),
  (4, 3),
  (5, 6),
  (6, 3),
  (11, 3),
])
def test_DefaultDeliveryFee(quantity, delivery_distance):
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=quantity))
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 3.50
