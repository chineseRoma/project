/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2021-12-26 21:21:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `messages`
-- ----------------------------
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
  `message` longtext NOT NULL,
  `time` varchar(20) DEFAULT NULL,
  `id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of messages
-- ----------------------------
INSERT INTO `messages` VALUES ('fasdf', '2021-12-26 19:07:41', '1');
INSERT INTO `messages` VALUES ('fdas', '2021-12-26 19:07:43', '2');
INSERT INTO `messages` VALUES ('asdfas', '2021-12-26 19:07:46', '3');
INSERT INTO `messages` VALUES ('asdfasdf', '2021-12-26 19:07:53', '4');
INSERT INTO `messages` VALUES ('今天是个好日子\r\n', '2021-12-26 20:08:48', '5');
INSERT INTO `messages` VALUES ('', '2021-12-26 20:08:03', '6');
