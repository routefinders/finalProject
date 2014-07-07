-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2014 at 11:03 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dps`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `name` varchar(60) NOT NULL,
  `username` varchar(80) NOT NULL,
  `password` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `username`, `password`, `email`) VALUES
('sentiking', 'sentiking', '*06C06205CE0BBC4E25225742780BA', 'sentiking@yahoo.com'),
('prakash', 'parumaster', 'parumaster', 'aryalprakash@gmail.com'),
('nabin', 'nabin', 'nabin', 'nabin.khadka@gmail.com'),
('bipin', 'bipin', 'bipin', 'bipinpandye11@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `deliveruser`
--

CREATE TABLE IF NOT EXISTS `deliveruser` (
  `name` varchar(60) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(30) NOT NULL,
  `contact_no` varchar(30) NOT NULL,
  `Date` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE IF NOT EXISTS `orders` (
  `customer_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `productName` varchar(30) NOT NULL,
  `source_lat` float(10,6) NOT NULL,
  `source_lng` float(10,6) NOT NULL,
  `dest_lat` float(10,6) NOT NULL,
  `dest_lng` float(10,6) NOT NULL,
  `contact_number` varchar(30) NOT NULL,
  `quantity` int(5) NOT NULL,
  `date_order` date NOT NULL,
  `date_deliver` date NOT NULL,
  `delivery status` varchar(30) NOT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(30) NOT NULL,
  `contact_no` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`customer_id`, `name`, `email`, `password`, `contact_no`, `address`) VALUES
(1, 'sanjay', 'sentiraut@gmail.com', '*01918040200C71B3DF14BC6878450', '9841484673', 'kopundole.lalitpur'),
(2, 'senti', 'sentiking@yahoo.com', '*01918040200C71B3DF14BC6878450', '9849096390', 'chakupat');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
