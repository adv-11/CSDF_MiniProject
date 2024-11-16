import logging

# Configure the logger
logging.basicConfig(filename='sample.log', level=logging.INFO, format='[%(asctime)s] %(message)s')

# Create a logger
logger = logging.getLogger('my_logger')

# Log messages
logger.info('Advait - Login failed: Incorrect password (password=13579)')
logger.info('AdminUser - Login successful')
logger.info('User456 - Access denied: Unauthorized IP address (192.168.1.100)')
logger.info('User789 - File access: /sensitive-data/file.txt')
logger.info('Hacker1 - Port scan detected: Target IP (10.0.0.5)')
logger.info('AdminUser - Account locked: Multiple failed login attempts')
logger.info('Advait - Password change: Successful (new_password=abc123)')
logger.info('User456 - Logout')
logger.info('Hacker2 - SQL injection attempt: Detected in the web application')
logger.info('User789 - Critical system error: Application crashed')