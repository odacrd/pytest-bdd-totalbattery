import json
import os
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.definitions import ROOT_URL
from config.definitions import ROOT_DIR


@pytest.fixture
def root_url():
    return ROOT_URL


def get_config_file_path():
    return os.path.join(ROOT_DIR, 'config', 'browser_config.json')


@pytest.fixture
def config(scope='session'):
    with open(get_config_file_path()) as config_file:
        config = json.load(config_file)

    return config


def set_options(opts, config):
    if config['mode'] == 'Headless':
        opts.add_argument('--headless=new')
    opts.page_load_strategy = config['page_load_strategy']


@pytest.fixture()
def driver(config):
    if config['browser'] == 'Chrome':
        chromeOptionsMap = {}
        chromeOptionsMap["credentials_enable_service"] = False
        chromeOptionsMap["password_manager_enabled"] = False
        chromeOptionsMap["autofill.profile_enabled"] = False
        opts = Options()
        opts.add_experimental_option("prefs", chromeOptionsMap)
        # opts.add_argument("--headless=new")
        # opts = webdriver.ChromeOptions()
        set_options(opts, config)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
        # driver = webdriver.Chrome(options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        set_options(opts, config)
        driver = webdriver.Firefox(options=opts)
    elif config['browser'] == 'Edge':
        opts = webdriver.EdgeOptions()
        set_options(opts, config)
        driver = webdriver.Edge(options=opts)
    else:
        raise Exception(f'Unknown type of browser')


    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
