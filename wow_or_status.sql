CREATE TABLE `wow_or_status_copy` (
  `ordernumber` varchar(50) NOT NULL DEFAULT '',
  `wow_status` varchar(250) DEFAULT NULL,
  `warehouse` varchar(200) DEFAULT NULL,
  `date_updated` datetime DEFAULT NULL,
  PRIMARY KEY (`ordernumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
