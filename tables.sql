CREATE DATABASE IF NOT EXISTS insurance;
USE insurance;

-- Disable foreign key checks to avoid dependency errors during creation
SET FOREIGN_KEY_CHECKS=0;

-- 1. Customers: Basic customer info
CREATE TABLE Customers (
    customer_id CHAR(10) PRIMARY KEY,
    first_name CHAR(50),
    last_name CHAR(50),
    gender CHAR(6),
    dob CHAR(10), -- YYYY-MM-DD
    address CHAR(100),
    city CHAR(50),
    state CHAR(20),
    zip CHAR(10),
    phone CHAR(15),
    email CHAR(50)
) ENGINE=InnoDB;

-- 2. Agents: Insurance agents info
CREATE TABLE Agents (
    agent_id CHAR(10) PRIMARY KEY,
    first_name CHAR(50),
    last_name CHAR(50),
    phone CHAR(15),
    email CHAR(50),
    address CHAR(100)
) ENGINE=InnoDB;

-- 3. Policies: Insurance policies sold to customers
CREATE TABLE Policies (
    policy_id CHAR(15) PRIMARY KEY,
    customer_id CHAR(10),
    policy_type CHAR(20), -- e.g. Auto, Health, Life
    policy_start_date CHAR(10),
    policy_end_date CHAR(10),
    premium_amount CHAR(15),
    policy_status CHAR(20), -- active, expired, canceled
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
) ENGINE=InnoDB;

-- 5. Claims: Claims made by customers on policies
CREATE TABLE Claims (
    claim_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    claim_type CHAR(20), -- accident, theft, fire, etc.
    claim_date CHAR(10),
    claim_amount CHAR(15),
    claim_status CHAR(20), -- pending, approved, denied
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 6. Payments: Payment transactions for policies
CREATE TABLE Payments (
    payment_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    payment_date CHAR(10),
    amount_paid CHAR(15),
    payment_method CHAR(20), -- credit card, cash, etc.
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 4. Policy_Agents: Many-to-many between policies and agents
CREATE TABLE Policy_Agents (
    policy_id CHAR(15),
    agent_id CHAR(10),
    PRIMARY KEY (policy_id, agent_id),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id),
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
) ENGINE=InnoDB;

-- 7. Auto_Policies: Specific details for auto insurance policies
CREATE TABLE Auto_Policies (
    auto_policy_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    make CHAR(30),
    model CHAR(30),
    year CHAR(4),
    liability_amount CHAR(15),
    uninsured_motorist CHAR(15),
    underinsured_motorist CHAR(15),
    med_pay CHAR(15),
    collision_damage CHAR(15),
    named_insured CHAR(100),
    additional_driver CHAR(100),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 8. Homeowners_Policies: Specific details for homeowners insurance
CREATE TABLE Homeowners_Policies (
    homeowners_policy_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    liability_amount CHAR(15),
    property_damage_amount CHAR(15),
    premium CHAR(15),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 9. Renters_Policies: Specific details for renters insurance
CREATE TABLE Renters_Policies (
    renters_policy_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    liability_amount CHAR(15),
    property_damage_amount CHAR(15),
    premium CHAR(15),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 10. Life_Insurance_Policies: Specific details for life insurance
CREATE TABLE Life_Insurance_Policies (
    life_policy_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    premium_amount CHAR(15),
    benefit_amount CHAR(15),
    beneficiary CHAR(100),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 11. Claim_Investigations: Details about claim investigations
CREATE TABLE Claim_Investigations (
    investigation_id CHAR(15) PRIMARY KEY,
    claim_id CHAR(15),
    investigator_name CHAR(100),
    investigation_date CHAR(10),
    findings CHAR(255),
    FOREIGN KEY (claim_id) REFERENCES Claims(claim_id)
) ENGINE=InnoDB;

-- 12. Claim_Status_Reasons: Reasons for claim status changes
CREATE TABLE Claim_Status_Reasons (
    reason_id CHAR(10) PRIMARY KEY,
    reason_description CHAR(100)
) ENGINE=InnoDB;

-- 13. Claim_Status_History: History of claim status changes
CREATE TABLE Claim_Status_History (
    claim_id CHAR(15),
    status CHAR(20),
    reason_id CHAR(10),
    status_date CHAR(10),
    PRIMARY KEY (claim_id, status_date),
    FOREIGN KEY (claim_id) REFERENCES Claims(claim_id),
    FOREIGN KEY (reason_id) REFERENCES Claim_Status_Reasons(reason_id)
) ENGINE=InnoDB;

-- 14. Customer_Payments: Payment info related to customers (e.g. billing)
CREATE TABLE Customer_Payments (
    payment_id CHAR(15) PRIMARY KEY,
    customer_id CHAR(10),
    payment_date CHAR(10),
    amount CHAR(15),
    payment_method CHAR(20),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
) ENGINE=InnoDB;

-- 15. Beneficiaries: Beneficiaries for life insurance policies
CREATE TABLE Beneficiaries (
    beneficiary_id CHAR(15) PRIMARY KEY,
    life_policy_id CHAR(15),
    beneficiary_name CHAR(100),
    relationship CHAR(50),
    percentage CHAR(5),
    FOREIGN KEY (life_policy_id) REFERENCES Life_Insurance_Policies(life_policy_id)
) ENGINE=InnoDB;

-- 16. Policy_Coverages: Coverage details for policies
CREATE TABLE Policy_Coverages (
    coverage_id CHAR(15) PRIMARY KEY,
    policy_id CHAR(15),
    coverage_type CHAR(50),
    coverage_limit CHAR(15),
    premium CHAR(15),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id)
) ENGINE=InnoDB;

-- 17. Reinsurance_Contracts: Reinsurance contract details
CREATE TABLE Reinsurance_Contracts (
    contract_id CHAR(15) PRIMARY KEY,
    reinsurer_name CHAR(100),
    contract_start_date CHAR(10),
    contract_end_date CHAR(10),
    contract_amount CHAR(15)
) ENGINE=InnoDB;

-- 18. Policy_Reinsurance: Linking policies to reinsurance contracts
CREATE TABLE Policy_Reinsurance (
    policy_id CHAR(15),
    contract_id CHAR(15),
    PRIMARY KEY (policy_id, contract_id),
    FOREIGN KEY (policy_id) REFERENCES Policies(policy_id),
    FOREIGN KEY (contract_id) REFERENCES Reinsurance_Contracts(contract_id)
) ENGINE=InnoDB;

-- 19. Adjusters: Claim adjusters info
CREATE TABLE Adjusters (
    adjuster_id CHAR(10) PRIMARY KEY,
    first_name CHAR(50),
    last_name CHAR(50),
    experience_years CHAR(2),
    phone CHAR(15),
    email CHAR(50)
) ENGINE=InnoDB;

-- 20. Claims_Adjusters: Mapping claims to adjusters
CREATE TABLE Claims_Adjusters (
    claim_id CHAR(15),
    adjuster_id CHAR(10),
    PRIMARY KEY (claim_id, adjuster_id),
    FOREIGN KEY (claim_id) REFERENCES Claims(claim_id),
    FOREIGN KEY (adjuster_id) REFERENCES Adjusters(adjuster_id)
) ENGINE=InnoDB;

-- Re-enable foreign key checks after creation
SET FOREIGN_KEY_CHECKS=1;
