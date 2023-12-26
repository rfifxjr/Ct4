import pytest
import requests
import allure

BASE_URL = "https://dog.ceo/api"

@pytest.fixture
def random_dog_img():
    with allure.step("Получение случайного изображения"):
        response = requests.get(f"{BASE_URL}/breeds/image/random")
        data = response.json()
        return data.get('message')

@allure.feature("Dog API")
class TestDogAPI:

    @allure.title("Проверка статус-кода при получении случайного изображения")
    def test_get_rand_dog_img_code(self):
        with allure.step("Отправка запроса для получения случайного изображения"):
            response = requests.get(f"{BASE_URL}/breeds/image/random")
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

    @allure.title("Проверка статус-кода при получении всех изображений")
    def test_get_all_dog_img_code(self):
        with allure.step("Отправка запроса для получения всех изображений"):
            response = requests.get(f"{BASE_URL}/breeds/list/all")
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

    @allure.title("Проверка формата URL случайного изображения")
    def test_dog_url(self, random_dog_img):
        with allure.step("Проверка, что URL случайного изображения не является пустым"):
            assert random_dog_img is not None
        with allure.step("Проверка, что URL начинается с корректного префикса"):
            assert random_dog_img.startswith("https://images.dog.ceo")

    @allure.title("Получение изображений для определенной породы")
    def test_get_spec_breed(self):
        breed = "Boxer"
        with allure.step(f"Получение изображений для породы {breed}"):
            response = requests.get(f"{BASE_URL}/breed/{breed}/images")
        with allure.step("Проверка формата ответа"):
            data = response.json()
            assert "message" in data
            assert len(data["message"]) > 0

    @allure.title("Проверка формата изображения")
    def test_format(self):
        with allure.step("Получение случайного изображения"):
            response = requests.get(f"{BASE_URL}/breeds/image/random")
        with allure.step("Проверка формата ответа"):
            data = response.json()
            assert "message" in data
            img_url = data["message"]
            assert img_url.endswith(".jpg")
