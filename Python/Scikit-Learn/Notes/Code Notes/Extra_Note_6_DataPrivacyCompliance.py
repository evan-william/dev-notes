"""
Data Privacy and Compliance
============================
This file covers key concepts in data privacy regulations including GDPR, CCPA, and PIPL.
Note: This contains conceptual code examples for educational purposes.
"""

from datetime import datetime, timedelta
import json

# =============================================================================
# GDPR (GENERAL DATA PROTECTION REGULATION)
# =============================================================================

print("=" * 60)
print("GDPR - GENERAL DATA PROTECTION REGULATION (EU)")
print("=" * 60)

class GDPRCompliance:
    """
    GDPR is the EU's comprehensive data protection law.
    Key principle: Individuals have significant rights over their personal data.
    """
    
    def __init__(self):
        self.breach_notification_hours = 72
        self.user_data = {}  # Simulated database
    
    def right_to_access(self, user_id):
        """
        GDPR Right: Individuals can access their personal data
        
        Under GDPR, individuals have the right to:
        - Know what data is being processed
        - Obtain a copy of their data
        - Get information about how their data is used
        """
        print(f"\n📋 RIGHT TO ACCESS - User {user_id}")
        print("-" * 50)
        
        if user_id in self.user_data:
            print(f"Personal data for user {user_id}:")
            print(json.dumps(self.user_data[user_id], indent=2))
            return self.user_data[user_id]
        else:
            print(f"No data found for user {user_id}")
            return None
    
    def right_to_deletion(self, user_id):
        """
        GDPR Right: Right to be forgotten / Right to erasure
        
        Individuals can request deletion of their personal data when:
        - Data is no longer necessary for original purpose
        - They withdraw consent
        - They object to processing
        - Data was unlawfully processed
        """
        print(f"\n🗑️  RIGHT TO DELETION - User {user_id}")
        print("-" * 50)
        
        if user_id in self.user_data:
            deleted_data = self.user_data.pop(user_id)
            print(f"✓ Successfully deleted data for user {user_id}")
            print(f"Deleted records: {len(deleted_data)} fields")
            return True
        else:
            print(f"No data found for user {user_id}")
            return False
    
    def report_data_breach(self, breach_discovery_time):
        """
        GDPR Requirement: Report breaches within 72 hours
        
        Organizations must notify the supervisory authority of a data breach
        within 72 hours of becoming aware of it, unless the breach is unlikely
        to result in a risk to individuals' rights and freedoms.
        """
        print(f"\n🚨 DATA BREACH NOTIFICATION")
        print("-" * 50)
        
        current_time = datetime.now()
        time_since_breach = current_time - breach_discovery_time
        hours_since_breach = time_since_breach.total_seconds() / 3600
        
        print(f"Breach discovered: {breach_discovery_time}")
        print(f"Current time: {current_time}")
        print(f"Time elapsed: {hours_since_breach:.2f} hours")
        
        if hours_since_breach <= self.breach_notification_hours:
            print(f"✓ Within {self.breach_notification_hours}-hour reporting window")
            print("Status: COMPLIANT")
            return True
        else:
            print(f"✗ Exceeded {self.breach_notification_hours}-hour reporting window")
            print("Status: NON-COMPLIANT - May face penalties")
            return False

# Demonstration
gdpr = GDPRCompliance()

# Add sample user data
gdpr.user_data = {
    "user_001": {
        "name": "John Doe",
        "email": "john@example.com",
        "address": "123 Main St, Brussels, Belgium",
        "purchase_history": ["item1", "item2", "item3"]
    }
}

# Test GDPR rights
print("\n" + "=" * 60)
print("DEMONSTRATING GDPR RIGHTS")
print("=" * 60)

# 1. Right to Access
gdpr.right_to_access("user_001")

# 2. Right to Deletion
gdpr.right_to_deletion("user_001")

# Verify deletion
gdpr.right_to_access("user_001")

# 3. Breach Notification
print("\n--- Scenario 1: Timely reporting ---")
breach_time_1 = datetime.now() - timedelta(hours=48)
gdpr.report_data_breach(breach_time_1)

print("\n--- Scenario 2: Late reporting ---")
breach_time_2 = datetime.now() - timedelta(hours=100)
gdpr.report_data_breach(breach_time_2)

# =============================================================================
# CCPA (CALIFORNIA CONSUMER PRIVACY ACT)
# =============================================================================

print("\n\n" + "=" * 60)
print("CCPA - CALIFORNIA CONSUMER PRIVACY ACT (USA)")
print("=" * 60)

class CCPACompliance:
    """
    CCPA is California's comprehensive privacy law.
    Key principle: Consumers have control over their personal information.
    """
    
    def __init__(self):
        self.applies_to = [
            "For-profit businesses",
            "Operating in California",
            "Meeting revenue/data thresholds"
        ]
        self.revenue_threshold = 25_000_000  # $25 million
        self.consumer_threshold = 100_000    # 100k consumers/devices
        self.data_sale_opt_outs = {}
    
    def check_applicability(self, annual_revenue, num_consumers, revenue_from_data_sales):
        """
        CCPA applies to businesses that meet ANY of these criteria:
        1. Annual gross revenues > $25 million
        2. Buy/sell personal info of 100k+ consumers/devices
        3. Derive 50%+ of annual revenue from selling personal info
        """
        print(f"\n🏢 CCPA APPLICABILITY CHECK")
        print("-" * 50)
        print(f"Annual Revenue: ${annual_revenue:,}")
        print(f"Number of Consumers: {num_consumers:,}")
        print(f"Revenue from Data Sales: {revenue_from_data_sales}%")
        print()
        
        criterion_1 = annual_revenue > self.revenue_threshold
        criterion_2 = num_consumers >= self.consumer_threshold
        criterion_3 = revenue_from_data_sales >= 50
        
        print(f"Criterion 1 (Revenue > $25M): {'✓ MET' if criterion_1 else '✗ Not met'}")
        print(f"Criterion 2 (100k+ consumers): {'✓ MET' if criterion_2 else '✗ Not met'}")
        print(f"Criterion 3 (50%+ from data sales): {'✓ MET' if criterion_3 else '✗ Not met'}")
        
        applies = criterion_1 or criterion_2 or criterion_3
        print(f"\nCCPA Applies: {'YES' if applies else 'NO'}")
        return applies
    
    def opt_out_of_sale(self, consumer_id):
        """
        CCPA Right: Right to opt-out of the sale of personal information
        
        This is a KEY right under CCPA. Consumers can prevent businesses
        from selling their personal data to third parties.
        
        Businesses must provide a "Do Not Sell My Personal Information" link.
        """
        print(f"\n🛑 OPT-OUT OF DATA SALE - Consumer {consumer_id}")
        print("-" * 50)
        
        self.data_sale_opt_outs[consumer_id] = {
            "opted_out": True,
            "timestamp": datetime.now(),
            "can_sell_data": False
        }
        
        print(f"✓ Consumer {consumer_id} has opted out of data sales")
        print("Their personal information will NOT be sold to third parties")
        return True
    
    def can_sell_consumer_data(self, consumer_id):
        """
        Check if a consumer's data can be sold
        """
        if consumer_id in self.data_sale_opt_outs:
            if self.data_sale_opt_outs[consumer_id]["opted_out"]:
                print(f"❌ Cannot sell data for consumer {consumer_id} - Opted out")
                return False
        
        print(f"✓ Can sell data for consumer {consumer_id}")
        return True

# Demonstration
ccpa = CCPACompliance()

print("\n" + "=" * 60)
print("DEMONSTRATING CCPA COMPLIANCE")
print("=" * 60)

# Test applicability
print("\n--- Example 1: Large tech company ---")
ccpa.check_applicability(
    annual_revenue=50_000_000,
    num_consumers=500_000,
    revenue_from_data_sales=30
)

print("\n--- Example 2: Small local business ---")
ccpa.check_applicability(
    annual_revenue=2_000_000,
    num_consumers=5_000,
    revenue_from_data_sales=10
)

# Test opt-out rights
print("\n--- Consumer exercising opt-out right ---")
ccpa.opt_out_of_sale("consumer_123")
ccpa.can_sell_consumer_data("consumer_123")
ccpa.can_sell_consumer_data("consumer_456")

# =============================================================================
# PIPL (PERSONAL INFORMATION PROTECTION LAW - CHINA)
# =============================================================================

print("\n\n" + "=" * 60)
print("PIPL - PERSONAL INFORMATION PROTECTION LAW (CHINA)")
print("=" * 60)

class PIPLCompliance:
    """
    PIPL is China's comprehensive data protection law.
    Key principle: Strict controls on data transfers outside China.
    """
    
    def __init__(self):
        self.approved_transfer_methods = [
            "Security assessment by Chinese authorities",
            "Personal Information Protection Certification",
            "Standard contractual clauses",
            "Individual consent"
        ]
        self.data_localization_required = True
    
    def assess_cross_border_transfer(self, data_type, destination_country, has_approval):
        """
        PIPL Requirement: Limit data transfers outside China
        
        Cross-border data transfers require:
        1. Security assessment by authorities OR
        2. Certification from approved organizations OR
        3. Standard contracts with foreign recipients OR
        4. Separate individual consent
        
        Critical or important data has stricter requirements.
        """
        print(f"\n🌍 CROSS-BORDER DATA TRANSFER ASSESSMENT")
        print("-" * 50)
        print(f"Data Type: {data_type}")
        print(f"Destination: {destination_country}")
        print(f"Has Approval/Certification: {has_approval}")
        print()
        
        if destination_country == "China":
            print("✓ Domestic transfer - No PIPL cross-border restrictions")
            return True
        
        if has_approval:
            print("✓ Transfer ALLOWED")
            print("Reason: Has proper approval/certification")
            return True
        else:
            print("❌ Transfer BLOCKED")
            print("Reason: Missing required approval for cross-border transfer")
            print("\nRequired:")
            for method in self.approved_transfer_methods:
                print(f"  - {method}")
            return False
    
    def data_localization_check(self, data_category, stored_in_china):
        """
        PIPL requires critical information infrastructure operators
        to store personal data collected in China within China.
        """
        print(f"\n💾 DATA LOCALIZATION CHECK")
        print("-" * 50)
        print(f"Data Category: {data_category}")
        print(f"Stored in China: {stored_in_china}")
        print()
        
        if stored_in_china:
            print("✓ COMPLIANT - Data is localized in China")
            return True
        else:
            print("⚠️  WARNING - Data localization may be required")
            print("Critical infrastructure operators MUST store data in China")
            return False

# Demonstration
pipl = PIPLCompliance()

print("\n" + "=" * 60)
print("DEMONSTRATING PIPL COMPLIANCE")
print("=" * 60)

# Test cross-border transfers
print("\n--- Scenario 1: Transfer with approval ---")
pipl.assess_cross_border_transfer(
    data_type="Customer Information",
    destination_country="Germany",
    has_approval=True
)

print("\n--- Scenario 2: Transfer without approval ---")
pipl.assess_cross_border_transfer(
    data_type="User Profiles",
    destination_country="United States",
    has_approval=False
)

print("\n--- Scenario 3: Domestic transfer ---")
pipl.assess_cross_border_transfer(
    data_type="Transaction Data",
    destination_country="China",
    has_approval=False
)

# Test data localization
print("\n--- Data localization scenarios ---")
pipl.data_localization_check("Critical Infrastructure Data", stored_in_china=True)
pipl.data_localization_check("Critical Infrastructure Data", stored_in_china=False)

# =============================================================================
# ACCOUNTABILITY PRINCIPLE
# =============================================================================

print("\n\n" + "=" * 60)
print("ACCOUNTABILITY PRINCIPLE")
print("=" * 60)

class AccountabilityFramework:
    """
    Accountability means organizations must:
    1. Be responsible for their data practices
    2. Demonstrate compliance with privacy laws
    3. Maintain documentation and records
    """
    
    def __init__(self):
        self.audit_log = []
        self.policies = {}
        self.training_records = {}
    
    def log_data_activity(self, activity_type, details):
        """
        Organizations must maintain records to demonstrate compliance
        """
        log_entry = {
            "timestamp": datetime.now(),
            "activity": activity_type,
            "details": details
        }
        self.audit_log.append(log_entry)
        print(f"✓ Logged: {activity_type}")
    
    def demonstrate_compliance(self):
        """
        Being accountable means showing evidence of compliance
        """
        print(f"\n📊 COMPLIANCE DEMONSTRATION")
        print("-" * 50)
        print(f"Total audit log entries: {len(self.audit_log)}")
        print(f"Privacy policies documented: {len(self.policies)}")
        print(f"Staff trained: {len(self.training_records)}")
        print("\nAccountability requires:")
        print("  ✓ Documentation of data practices")
        print("  ✓ Regular audits and assessments")
        print("  ✓ Staff training and awareness")
        print("  ✓ Incident response procedures")
        print("  ✓ Vendor management and oversight")

# Demonstration
accountability = AccountabilityFramework()
accountability.log_data_activity("Data Collection", "User registration form")
accountability.log_data_activity("Data Access", "User requested their data")
accountability.log_data_activity("Data Deletion", "User exercised right to erasure")
accountability.demonstrate_compliance()

# =============================================================================
# COMMON COMPLIANCE CHALLENGES
# =============================================================================

print("\n\n" + "=" * 60)
print("COMMON COMPLIANCE CHALLENGES FOR GLOBAL COMPANIES")
print("=" * 60)

challenges = {
    "Challenge 1": {
        "issue": "Ensuring consistent data practices across jurisdictions",
        "description": "Different countries have different privacy laws",
        "example": "GDPR (EU) vs CCPA (California) vs PIPL (China)",
        "solution": "Implement highest common standard or region-specific policies"
    },
    "Challenge 2": {
        "issue": "Managing data subject rights at scale",
        "description": "Handling access, deletion, and portability requests",
        "example": "Processing thousands of deletion requests efficiently",
        "solution": "Automated systems with audit trails"
    },
    "Challenge 3": {
        "issue": "Cross-border data transfers",
        "description": "Moving data between countries with different laws",
        "example": "EU data transferred to US servers",
        "solution": "Standard Contractual Clauses, adequacy decisions"
    },
    "Challenge 4": {
        "issue": "Vendor and third-party management",
        "description": "Ensuring partners are also compliant",
        "example": "Cloud providers, marketing platforms",
        "solution": "Due diligence, contracts, regular audits"
    }
}

for challenge, details in challenges.items():
    print(f"\n{challenge}: {details['issue']}")
    print(f"Description: {details['description']}")
    print(f"Example: {details['example']}")
    print(f"Solution: {details['solution']}")

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
GDPR (EU):
  - Right to access and delete personal data
  - 72-hour breach notification requirement
  - Applies to processing EU residents' data

CCPA (California):
  - Right to opt-out of data sales
  - Applies to large for-profit businesses in California
  - $25M revenue OR 100k consumers OR 50% revenue from data sales

PIPL (China):
  - Strict cross-border data transfer restrictions
  - Data localization requirements
  - Security assessments for international transfers

Accountability:
  - Organizations must demonstrate compliance
  - Maintain documentation and audit trails
  - Regular training and assessments

Global Challenges:
  - Consistent practices across jurisdictions
  - Managing rights requests at scale
  - Third-party vendor compliance
""")