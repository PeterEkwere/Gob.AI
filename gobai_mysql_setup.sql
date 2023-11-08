-- Prepares a mysql server for GobAI

CREATE DATABASE IF NOT EXISTS gobai_db;
CREATE USER IF NOT EXISTS 'peter'@'localhost' IDENTIFIED BY 'Peter201$';
GRANT ALL PRIVILEGES ON `gobai_db`.* TO 'peter'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'peter'@'localhost';
FLUSH PRIVILEGES;

USE gobai_db;

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `user_name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('00a11245-12fa-436e-9ccc-967417f8c30a','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail6@gmail.com','pwd6','Todd'),
('00e93fc3-53ff-4da4-8e72-faa5216f81bb','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail28@gmail.com','pwd28','Richard'),
('150e591e-486b-48ee-be42-4aecba665020','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail23@gmail.com','pwd23','Cecilia'),
('30a890e4-a62c-44f9-abc0-07e2c74021da','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail2@gmail.com','pwd2','David'),
('32c11d3d-99a1-4406-ab41-7b6ccb7dd760','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail18@gmail.com','pwd18','Susan'),
('3ea61b06-e22a-459b-bb96-d900fb8f843a','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail8@gmail.com','pwd8','Melissa'),
('3fda0d5c-fea4-4920-bc91-6e6c6663d161','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail12@gmail.com','pwd12','Robert'),
('426624f6-84a9-4ec4-84f3-7655dc70e86e','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail19@gmail.com','pwd19','Gail'),
('fa44780d-ac48-41ab-9dd0-ac54a15755cf','2017-03-25 02:17:06','2017-03-25 02:17:06','noemail20@gmail.com','pwd20','Leon');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-23  0:14:51
