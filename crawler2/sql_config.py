"""
CREATE TABLE `el` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `thread_number` int(11) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `get_text` mediumtext DEFAULT NULL,
  `property` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


class SQLConfig:
    con = 'mysql+pymysql://root:@127.0.0.1:3306/crawlers?charset=utf8'
