-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 27, 2025 at 05:22 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1clouddbaudiohidepy`
--

-- --------------------------------------------------------

--
-- Table structure for table `filetb`
--

CREATE TABLE `filetb` (
  `id` bigint(20) NOT NULL auto_increment,
  `OwnerName` varchar(250) NOT NULL,
  `FileInfo` varchar(500) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `Pukey` varchar(250) NOT NULL,
  `Pvkey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `filetb`
--


-- --------------------------------------------------------

--
-- Table structure for table `ownertb`
--

CREATE TABLE `ownertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `ownertb`
--


-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `regtb`
--


-- --------------------------------------------------------

--
-- Table structure for table `userfiletb`
--

CREATE TABLE `userfiletb` (
  `id` bigint(20) NOT NULL auto_increment,
  `FileId` varchar(250) NOT NULL,
  `OwnerName` varchar(250) NOT NULL,
  `Filename` varchar(250) NOT NULL,
  `PrKey` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `ImageName` varchar(250) NOT NULL,
  `Imagedkey` varchar(250) NOT NULL,
  `Unhidekey` varchar(250) NOT NULL,
  `Decryptkey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `userfiletb`
--

