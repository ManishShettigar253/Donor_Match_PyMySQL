-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2024 at 09:22 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bdc`
--

-- --------------------------------------------------------

--
-- Table structure for table `bloodcheck`
--

CREATE TABLE `bloodcheck` (
  `id` int(3) NOT NULL,
  `recipient` varchar(2) NOT NULL,
  `rage` int(3) NOT NULL,
  `rweight` int(3) NOT NULL,
  `donator` varchar(2) NOT NULL,
  `result` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bloodcheck`
--

INSERT INTO `bloodcheck` (`id`, `recipient`, `rage`, `rweight`, `donator`, `result`) VALUES
(3, 'B-', 5, 5, 'AB', 'Cannot Donate'),
(4, 'B+', 67, 67, 'B+', 'Can Donate'),
(5, 'A+', 45, 55, 'A+', 'Can Donate'),
(6, 'A+', 45, 55, 'AB', 'Cannot Donate'),
(7, 'A-', 89, 98, 'A-', 'Can Donate'),
(8, 'A-', 89, 9, 'A-', 'Cannot Donate'),
(9, 'B-', 67, 87, 'B+', 'Cannot Donate'),
(10, 'B-', 67, 87, 'B-', 'Can Donate'),
(11, 'A+', 67, 88, 'A+', 'Cannot Donate'),
(12, 'A+', 67, 88, 'A+', 'Cannot Donate'),
(13, 'B+', 67, 98, 'A-', 'Cannot Donate'),
(14, 'B+', 67, 98, 'B+', 'Cannot Donate'),
(15, 'A+', 56, 55, 'A+', 'Cannot Donate'),
(16, 'A+', 56, 55, 'A+', 'Can Donate'),
(17, 'A+', 564, 55, 'A+', 'Cannot Donate'),
(18, 'A+', 22, 78, 'A+', 'Can Donate'),
(19, 'A+', 81, 44, 'A+', 'Cannot Donate');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bloodcheck`
--
ALTER TABLE `bloodcheck`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bloodcheck`
--
ALTER TABLE `bloodcheck`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
