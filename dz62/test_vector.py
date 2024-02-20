import pytest
from vector import Vector


@pytest.fixture
def sample_vectors():
    vector1 = Vector(1, 2, 3)
    vector2 = Vector(4, 5, 6)
    return vector1, vector2


def test_vector_creation():
    v = Vector(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3


def test_vector_equality(sample_vectors):
    vector1, vector2 = sample_vectors
    assert vector1 == Vector(1, 2, 3)
    assert vector1 != vector2


def test_vector_addition(sample_vectors):
    vector1, vector2 = sample_vectors
    result = vector1 + vector2
    assert result == Vector(5, 7, 9)


def test_vector_subtraction(sample_vectors):
    vector1, vector2 = sample_vectors
    result = vector2 - vector1
    assert result == Vector(3, 3, 3)


def test_vector_inplace_operations(sample_vectors):
    vector1, vector2 = sample_vectors
    vector1 += vector2
    assert vector1 == Vector(5, 7, 9)

    vector2 -= vector1
    assert vector2 == Vector(-1, -2, -3)


def test_vector_multiplication(sample_vectors):
    vector1, vector2 = sample_vectors
    result = vector1 * 2
    assert result == Vector(2, 4, 6)

    dot_product = vector1 * vector2
    assert dot_product == 32


def test_vector_negation(sample_vectors):
    vector1, vector2 = sample_vectors
    neg_vector = -vector1
    assert neg_vector == Vector(-1, -2, -3)
