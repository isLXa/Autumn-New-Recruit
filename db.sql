CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '姓名',
  `tel` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '手机号',
  `sex` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '性别',
  `grade` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '年级',
  `college` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '学院',
  `dormitory` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '宿舍',
  `first` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '第一志愿',
  `second` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '第二志愿',
  `adjust` tinyint(1) NOT NULL COMMENT '是否服从调剂',
  `description` varchar(255) COLLATE utf8mb4_general_ci NOT NULL COMMENT '自我介绍',
   PRIMARY KEY (`id`),
   UNIQUE KEY `tel` (`tel`),
   KEY `name` (`name`,`tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
​
CREATE TABLE `admin` (
    `id` INT NOT NULL AUTO_INCREMENT ,
    `username` VARCHAR(255) NOT NULL ,
    `password` VARCHAR(255) NOT NULL ,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;