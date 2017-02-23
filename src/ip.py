"""
This is an IP module. It's for the class to live.
"""
import logging
from logging import DEBUG, NOTSET

logger = logging.getLogger('route-table-visualization/ip.py')
if __name__ == '__main__':
  logger.setLevel(NOTSET)

var: int = 3

class IPv4:
    """
    This is the class for IP
    """

    first: int
    second: int
    third: int
    fourth: int

    

    def __init__(self, address: str):
        """
        This method initializes the class
        """
        split_address = address.split('.')
        logger.debug(split_address)
        if len(split_address) != 4:
          raise Exception('The number of dots is not 4 in the supplied address.')
        self.first = int(split_address[0])
        
    # def 


if __name__ == '__main__':
  logger.warning('We are testing!')
  ip1 = IPv4('0.0.0.0')
  print(ip1.first)
  
