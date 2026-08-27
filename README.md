# Adithya -- PES1UG24CS021

## PROBLEM STATEMENT #21 | Smart Cities, Transport & Logistics

### EV Charging Station Reservation System

## 1. Problem Context & Overview

Electric vehicle drivers require a navigation and reservation portal to locate compatible charging sockets (CCS, CHAdeMO, Type 2), reserve guaranteed time slots, and calculate dynamic power rates.

**Target Stakeholders / Actors:**
- EV Driver
- Station Operator

## 2. Sample Functional Requirement (FR) Guideline

**Sample Requirement:** FR-001 [Priority: High]

**Description:**  
The system shall match the driver vehicle connector type with available station chargers and reserve a 30-minute charging window.

**Sample Acceptance Criteria:**
- **Pass:** Incompatible connector plugs hidden from driver.
- **Fail:** Two vehicles booked for same socket concurrently.

## 3. Sample Non-Functional Requirement (NFR) Guideline

**Sample Requirement:** NFR-001 [Type: Performance & Security]

**Description:**  
The system shall automatically release locked sockets and apply a penalty if the driver fails to plug in within 10 minutes of slot start.

**Sample Acceptance Criteria:**  
- **Pass:** Benchmarking tests confirm target latency and security standards under simulated peak load.
