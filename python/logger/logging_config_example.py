# coding: utf-8
# logger_config_example.py

import logging
import logging.config

# 설정 파일 읽어 오기 
logging.config.fileConfig('logging.conf')

# 로거 생성 및 로그 레벨 설정, 핸들러 추가
logger = logging.getLogger(__name__)

# 로그 메세지 출력  
logger.debug('이 메세지는 개발자만 이해해요.')
logger.info('생각대로 동작하고 있어요.')
logger.warn('곧 문제가 생길 가능성이 높습니다.')
logger.error('문제가 생겼어요. 기능이 동작하지 않습니다.')
logger.critical('시스템이 다운됩니다!!!')

