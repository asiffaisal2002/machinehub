-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2026 at 03:39 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `machine`
--

-- --------------------------------------------------------

--
-- Table structure for table `addproduct`
--

CREATE TABLE `addproduct` (
  `proid` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `proname` varchar(30) NOT NULL,
  `promodel` varchar(30) NOT NULL,
  `procompany` varchar(30) NOT NULL,
  `proimage` varchar(255) NOT NULL,
  `proprice` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addproduct`
--

INSERT INTO `addproduct` (`proid`, `sid`, `proname`, `promodel`, `procompany`, `proimage`, `proprice`) VALUES
(2, 1, 'Drill Machine', '2019', 'IBell', '/media/81N4Cj%2Bl8cL._AC_UL480_QL65_.jpg', 2000),
(4, 1, 'Cutter', '2019', 'Black Decker', '/media/m1%20(1).webp', 3500),
(5, 4, 'machinery ', '2018', 'bosch', '/media/Goku.jpg', 100),
(6, 4, 'machinery ', '2018', 'bosch', '/media/Goku_DRD5bjt.jpg', 100),
(7, 4, 'tester', '2017', 'bosch', '/media/20230810_215012.jpg', 2000);

-- --------------------------------------------------------

--
-- Table structure for table `addrenting`
--

CREATE TABLE `addrenting` (
  `rid` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `rname` varchar(50) NOT NULL,
  `rbrand` varchar(50) NOT NULL,
  `rimage` varchar(500) NOT NULL,
  `rusage` varchar(300) NOT NULL,
  `rprice` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addrenting`
--

INSERT INTO `addrenting` (`rid`, `sid`, `rname`, `rbrand`, `rimage`, `rusage`, `rprice`) VALUES
(1, 4, 'Cutting Machine', 'Black Decker', '/media/71FuS3LQaaL._AC_UL480_FMwebp_QL65__NV3VOFb.webp', 'cutting tiles and wood', 500),
(2, 4, 'Cutting Machine', 'IBell', '/media/61MSLcU9GWS._AC_UL480_FMwebp_QL65_.webp', 'cutting tiles and wood', 400);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` varchar(25) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `role`) VALUES
('admin@gmail.com', 'admin', 'admin'),
('asif@gmail.com', 'asif', 'user'),
('hasna@gmali.com', 'hasna', 'staff'),
('yasin@gmail.com', 'yasin', 'user'),
('sahla@gmail.com', 'sahla', 'user'),
('satheesh@gmail.com', 'satheesh', 'staff'),
('unni@gmail.com', 'unni', 'staff'),
('aron@gmail.com', 'aron', 'user'),
('asna@gmail.com', 'asnasichu', 'staff');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pid` int(11) NOT NULL,
  `purid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `ctype` varchar(30) NOT NULL,
  `cnumber` varchar(30) NOT NULL,
  `cvv` varchar(30) NOT NULL,
  `amount` varchar(30) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pid`, `purid`, `uid`, `ctype`, `cnumber`, `cvv`, `amount`) VALUES
(1, 8, 1, 'debit', '1234123412341234', '122', ''),
(2, 8, 1, 'debit', '1234123412341234', '122', ''),
(3, 8, 1, 'debit', '1234123412341234', '122', ''),
(4, 11, 1, 'debit', '1234123412341234', '111', ''),
(5, 0, 3, 'debit', '1264274274741814', '432', '');

-- --------------------------------------------------------

--
-- Table structure for table `purchase`
--

CREATE TABLE `purchase` (
  `purid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `rid` int(11) NOT NULL,
  `purname` varchar(30) NOT NULL,
  `purplace` varchar(40) NOT NULL,
  `puraddress` varchar(50) NOT NULL,
  `purmobile` varchar(30) NOT NULL,
  `pincode` varchar(30) NOT NULL,
  `status` varchar(25) NOT NULL,
  `pstatus` varchar(25) NOT NULL,
  `dstatus` varchar(25) NOT NULL DEFAULT 'Pending',
  `sid` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `purchase`
--

INSERT INTO `purchase` (`purid`, `uid`, `rid`, `purname`, `purplace`, `puraddress`, `purmobile`, `pincode`, `status`, `pstatus`, `dstatus`, `sid`) VALUES
(1, 3, 2, 'rijan', 'karimpadam', 'rijan house karimpadam', '7564936654', '678876', '', '', 'Pending', NULL),
(2, 3, 2, 'hasna v,f', 'karimpadam', 'hasna house karimpadam', '9744705314', '678876', '', '', 'Pending', NULL),
(3, 3, 4, 'asif', 'kochukadav', 'asif house kochukadav', '09567127931', '680734', '', '', 'Pending', NULL),
(4, 3, 2, 'asif', 'kochukadav', 'asif house kochukadav', '09567127931', '680734', '', '', 'Pending', NULL),
(5, 3, 2, 'asif', 'kochukadav', 'asif house kochukadav', '09567127931', '680734', '', '', 'Pending', NULL),
(6, 3, 2, 'asif', 'kochukadav', 'asif house kochukadav', '09567127931', '680734', '', '', 'Pending', NULL),
(7, 3, 2, 'asif', 'kochukadav', 'asif house kochukadav', '09567127931', '680734', '', '', 'Pending', NULL),
(8, 1, 2, 'anu', 'sdcdsc', 'sdcdscs', '987654321', '123456', 'Ordered', '', 'Pending', NULL),
(9, 1, 2, 'resmi', 'asdsf', 'pereppadam', '09876453000', '098765', 'Ordered', '', 'Pending', NULL),
(10, 1, 2, 'resmi', 'asdsf', 'pereppadam', '09876453000', '098765', 'Ordered', 'Not Paid', 'Pending', NULL),
(11, 1, 4, 'resmi', 'asdsf', 'pereppadam', '09876453000', '098765', 'Ordered', 'Paid', 'Pending', NULL),
(12, 3, 2, 'sahala', 'paravur', 'paravurhouse', '226571818177', '680342', 'Ordered', 'Not Paid', 'Pending', 1),
(13, 3, 5, 'sahalaa', 'paravur', 'paravu4hosuee', '167268348', '362726', 'Ordered', 'Not Paid', 'Delivered', 4);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `uid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `place` varchar(30) NOT NULL,
  `Address` varchar(60) NOT NULL,
  `email` varchar(30) NOT NULL,
  `mobno` varchar(25) NOT NULL,
  `password` varchar(10) NOT NULL,
  `cpassword` varchar(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`uid`, `name`, `place`, `Address`, `email`, `mobno`, `password`, `cpassword`) VALUES
(1, 'asif', 'kochukadav', 'asif house new york', 'asif@gmail.com', '9567127931', 'asif', 'asif'),
(2, 'yasin', 'paravoor', 'yasin house california', 'yasin@gmail.com', '8765876444', 'yasin', 'yasin'),
(3, 'sahla', 'karimpadam', 'sahla house karimpadam', 'sahla@gmail.com', '9876543210', 'sahla', 'sahla'),
(4, 'aron', 'nedumbassery', 'nedumbahouse', 'aron@gmail.com', '75568787872', 'aron', 'aron');

-- --------------------------------------------------------

--
-- Table structure for table `rent`
--

CREATE TABLE `rent` (
  `rentid` int(11) NOT NULL,
  `proid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `mob` varchar(25) NOT NULL,
  `pname` varchar(25) NOT NULL,
  `ndays` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `tamount` int(11) NOT NULL,
  `status` varchar(25) NOT NULL,
  `pstatus` varchar(25) NOT NULL,
  `sid` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rent`
--

INSERT INTO `rent` (`rentid`, `proid`, `uid`, `name`, `mob`, `pname`, `ndays`, `amount`, `tamount`, `status`, `pstatus`, `sid`) VALUES
(1, 2, 1, 'resmi', '09876453000', 'Drill Machine', 2, 2000, 4000, 'Processing', 'Paid', 3),
(2, 1, 1, 'resmi', '09876453000', 'Cutting Machine', 5, 500, 2500, 'Processing', 'Not Paid', 3),
(3, 1, 3, 'sahla', '9765416167', 'Cutting Machine', 12, 500, 6000, 'Processing', 'Paid', 4);

-- --------------------------------------------------------

--
-- Table structure for table `rentpayment`
--

CREATE TABLE `rentpayment` (
  `pid` int(11) NOT NULL,
  `rid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `ctype` varchar(25) NOT NULL,
  `cnumber` varchar(25) NOT NULL,
  `cvv` varchar(25) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rentpayment`
--

INSERT INTO `rentpayment` (`pid`, `rid`, `uid`, `ctype`, `cnumber`, `cvv`) VALUES
(1, 1, 1, 'credit', '1234123412341234', '111'),
(2, 3, 3, 'debit', '12345678912345', '456');

-- --------------------------------------------------------

--
-- Table structure for table `staffregister`
--

CREATE TABLE `staffregister` (
  `sid` int(11) NOT NULL,
  `sname` varchar(20) NOT NULL,
  `smobno` varchar(20) NOT NULL,
  `semail` varchar(25) NOT NULL,
  `staffimage` varchar(300) NOT NULL,
  `password` varchar(20) NOT NULL,
  `cpassword` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staffregister`
--

INSERT INTO `staffregister` (`sid`, `sname`, `smobno`, `semail`, `staffimage`, `password`, `cpassword`) VALUES
(4, 'hasna ', '09744705314', 'hasna@gmali.com', '/media/918826.jpg', 'hasna', 'hasna'),
(3, 'satheesh', '09876546721', 'satheesh@gmail.com', '/media/cristiano-ronaldo-5-163142408316x9.jpg', 'satheesh', 'satheesh'),
(5, 'unni', '98276522727', 'unni@gmail.com', '/media/20230810_215015.jpg', 'unni', 'unni'),
(6, 'asna', '7765453456', 'asna@gmail.com', '/media/20230810_215012_wlXLzLw.jpg', 'asnasichu', 'asnasichu');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addproduct`
--
ALTER TABLE `addproduct`
  ADD PRIMARY KEY (`proid`);

--
-- Indexes for table `addrenting`
--
ALTER TABLE `addrenting`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `purchase`
--
ALTER TABLE `purchase`
  ADD PRIMARY KEY (`purid`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`uid`);

--
-- Indexes for table `rent`
--
ALTER TABLE `rent`
  ADD PRIMARY KEY (`rentid`);

--
-- Indexes for table `rentpayment`
--
ALTER TABLE `rentpayment`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `staffregister`
--
ALTER TABLE `staffregister`
  ADD PRIMARY KEY (`sid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addproduct`
--
ALTER TABLE `addproduct`
  MODIFY `proid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `addrenting`
--
ALTER TABLE `addrenting`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `purchase`
--
ALTER TABLE `purchase`
  MODIFY `purid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `rent`
--
ALTER TABLE `rent`
  MODIFY `rentid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `rentpayment`
--
ALTER TABLE `rentpayment`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `staffregister`
--
ALTER TABLE `staffregister`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
