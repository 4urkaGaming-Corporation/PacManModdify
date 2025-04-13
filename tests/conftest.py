import pytest
import pygame


@pytest.fixture(scope="session", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()
