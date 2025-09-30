"""
Responsible AI and Ethics
=========================
This file covers principles and practices for developing ethical AI systems.
"""

import random
import numpy as np
from collections import Counter

# =============================================================================
# BIAS IN TRAINING DATA
# =============================================================================

print("=" * 60)
print("BIAS IN TRAINING DATA - THE PRIMARY SOURCE OF AI BIAS")
print("=" * 60)

class BiasDetection:
    """
    The most common source of unintended bias in generative AI is
    the QUALITY and COMPOSITION of the training data.
    
    Biased data leads to biased models.
    """
    
    def analyze_dataset_bias(self, dataset_demographics):
        """
        Analyze representation in training data
        """
        print(f"\n📊 DATASET COMPOSITION ANALYSIS")
        print("-" * 50)
        
        total_samples = sum(dataset_demographics.values())
        
        print(f"Total samples: {total_samples}")
        print("\nGroup representation:")
        
        for group, count in dataset_demographics.items():
            percentage = (count / total_samples) * 100
            print(f"  {group}: {count} ({percentage:.1f}%)")
            
            if percentage < 10:
                print(f"    ⚠️  WARNING: {group} is underrepresented!")
        
        # Check for severe imbalance
        max_count = max(dataset_demographics.values())
        min_count = min(dataset_demographics.values())
        imbalance_ratio = max_count / min_count if min_count > 0 else float('inf')
        
        print(f"\nImbalance ratio: {imbalance_ratio:.2f}:1")
        
        if imbalance_ratio > 10:
            print("❌ SEVERE BIAS RISK - Major representation imbalance")
        elif imbalance_ratio > 3:
            print("⚠️  MODERATE BIAS RISK - Significant imbalance")
        else:
            print("✓ ACCEPTABLE - Relatively balanced representation")
        
        return imbalance_ratio

# Example: Biased dataset
print("\n--- Example 1: Biased Hiring Dataset ---")
biased_hiring_data = {
    "Male Engineers": 8500,
    "Female Engineers": 1200,
    "Male Nurses": 800,
    "Female Nurses": 3500
}

bias_detector = BiasDetection()
bias_detector.analyze_dataset_bias(biased_hiring_data)

print("\n💡 Impact: A model trained on this data might:")
print("  - Associate 'engineer' primarily with males")
print("  - Associate 'nurse' primarily with females")
print("  - Make biased hiring recommendations")

# Example: Balanced dataset
print("\n--- Example 2: Improved Balanced Dataset ---")
balanced_hiring_data = {
    "Male Engineers": 5000,
    "Female Engineers": 4800,
    "Male Nurses": 2100,
    "Female Nurses": 2300
}

bias_detector.analyze_dataset_bias(balanced_hiring_data)

# =============================================================================
# HARMFUL CONTENT GENERATION
# =============================================================================

print("\n\n" + "=" * 60)
print("PRIMARY ETHICAL CONCERN: BIASED OR HARMFUL CONTENT")
print("=" * 60)

class HarmfulContentDetection:
    """
    A primary ethical concern in generative AI is its potential
    to generate biased or harmful content.
    
    This includes:
    - Discriminatory outputs
    - Harmful stereotypes
    - Offensive content
    - Misinformation
    """
    
    def __init__(self):
        self.harmful_patterns = [
            "discriminatory language",
            "stereotypes",
            "hate speech",
            "misinformation",
            "violence promotion",
            "privacy violations"
        ]
    
    def evaluate_output_safety(self, generated_text, check_stereotypes=True):
        """
        Evaluate generated content for potential harm
        """
        print(f"\n🔍 CONTENT SAFETY EVALUATION")
        print("-" * 50)
        print(f"Generated text: \"{generated_text}\"")
        print()
        
        concerns = []
        
        # Check for stereotypical language (simplified example)
        stereotypes = {
            "women are": "gender stereotype",
            "men are": "gender stereotype",
            "all [group]": "overgeneralization",
            "those people": "othering language"
        }
        
        text_lower = generated_text.lower()
        for pattern, issue in stereotypes.items():
            if pattern.replace("[group]", "") in text_lower:
                concerns.append(f"Potential {issue} detected")
        
        if concerns:
            print("⚠️  SAFETY CONCERNS DETECTED:")
            for concern in concerns:
                print(f"  - {concern}")
            print("\n❌ Output should be filtered or regenerated")
        else:
            print("✓ No obvious safety concerns detected")
            print("Note: Human review still recommended for production use")
        
        return len(concerns) == 0

# Examples
harm_detector = HarmfulContentDetection()

print("\n--- Example 1: Potentially harmful output ---")
harm_detector.evaluate_output_safety(
    "Women are naturally better at nursing because they are more caring"
)

print("\n--- Example 2: Neutral output ---")
harm_detector.evaluate_output_safety(
    "The candidate has extensive experience in software engineering"
)

# =============================================================================
# DIVERSE AND WELL-SELECTED TRAINING DATA
# =============================================================================

print("\n\n" + "=" * 60)
print("SOLUTION: DIVERSE AND WELL-SELECTED TRAINING DATA")
print("=" * 60)

class DataSelectionStrategy:
    """
    Responsible AI emphasizes using DIVERSE and WELL-SELECTED training data
    to avoid biased outputs.
    """
    
    def create_diverse_dataset(self, requirements):
        """
        Demonstrate principles of diverse data selection
        """
        print(f"\n📚 DIVERSE DATA SELECTION STRATEGY")
        print("-" * 50)
        
        print("Diversity Requirements:")
        for category, target in requirements.items():
            print(f"  {category}: {target}")
        
        print("\n✓ Best Practices:")
        practices = [
            "Include multiple demographic groups",
            "Ensure balanced representation",
            "Include edge cases and minority perspectives",
            "Validate data quality and accuracy",
            "Remove harmful or discriminatory content",
            "Document data sources and limitations",
            "Regular audits for emerging biases"
        ]
        
        for i, practice in enumerate(practices, 1):
            print(f"  {i}. {practice}")
        
        return practices

data_strategy = DataSelectionStrategy()

diversity_requirements = {
    "Geographic diversity": "Multiple countries and regions",
    "Demographic diversity": "All genders, ages, ethnicities",
    "Socioeconomic diversity": "Various income levels",
    "Language diversity": "Multiple languages and dialects",
    "Perspective diversity": "Different viewpoints and experiences"
}

data_strategy.create_diverse_dataset(diversity_requirements)

# =============================================================================
# ACCESSING HIGH-QUALITY, UNBIASED DATA
# =============================================================================

print("\n\n" + "=" * 60)
print("KEY CHALLENGE: ACCESSING HIGH-QUALITY, UNBIASED DATA")
print("=" * 60)

class DataQualityChallenge:
    """
    A key challenge in responsible AI is accessing high-quality,
    unbiased data for training models.
    """
    
    def assess_data_quality(self, data_source_info):
        """
        Evaluate data quality dimensions
        """
        print(f"\n🎯 DATA QUALITY ASSESSMENT")
        print("-" * 50)
        
        quality_dimensions = {
            "Accuracy": "Is the data correct and truthful?",
            "Completeness": "Are all necessary fields present?",
            "Consistency": "Is data uniform across sources?",
            "Timeliness": "Is the data current and relevant?",
            "Representativeness": "Does it reflect the real world?",
            "Provenance": "Is the source reliable and traceable?"
        }
        
        for dimension, question in quality_dimensions.items():
            score = data_source_info.get(dimension, 0)
            status = "✓" if score >= 7 else "⚠️" if score >= 4 else "❌"
            print(f"{status} {dimension} ({score}/10): {question}")
        
        avg_score = sum(data_source_info.values()) / len(data_source_info)
        print(f"\nOverall Quality Score: {avg_score:.1f}/10")
        
        if avg_score >= 7:
            print("✓ HIGH QUALITY - Suitable for training")
        elif avg_score >= 4:
            print("⚠️  MODERATE QUALITY - Needs improvement")
        else:
            print("❌ LOW QUALITY - Not suitable for training")
        
        return avg_score

quality_assessor = DataQualityChallenge()

# Example: Good data source
print("\n--- Example 1: High-Quality Data Source ---")
good_source = {
    "Accuracy": 9,
    "Completeness": 8,
    "Consistency": 9,
    "Timeliness": 8,
    "Representativeness": 7,
    "Provenance": 9
}
quality_assessor.assess_data_quality(good_source)

# Example: Poor data source
print("\n--- Example 2: Low-Quality Data Source ---")
poor_source = {
    "Accuracy": 4,
    "Completeness": 3,
    "Consistency": 5,
    "Timeliness": 3,
    "Representativeness": 2,
    "Provenance": 4
}
quality_assessor.assess_data_quality(poor_source)

# =============================================================================
# TRANSPARENCY IN DATA USE
# =============================================================================

print("\n\n" + "=" * 60)
print("TRANSPARENCY: FOSTERING TRUST AND ACCOUNTABILITY")
print("=" * 60)

class TransparencyFramework:
    """
    Transparency in data use is essential in Responsible AI primarily
    to FOSTER TRUST and ACCOUNTABILITY.
    
    Users should know:
    - What data is collected
    - How it's used
    - Who has access
    - How decisions are made
    """
    
    def create_data_transparency_report(self, model_info):
        """
        Generate transparency documentation
        """
        print(f"\n📋 DATA TRANSPARENCY REPORT")
        print("-" * 50)
        
        sections = {
            "Data Collection": [
                f"Data sources: {model_info.get('sources', 'Not specified')}",
                f"Collection period: {model_info.get('period', 'Not specified')}",
                f"Data volume: {model_info.get('volume', 'Not specified')}"
            ],
            "Data Usage": [
                f"Purpose: {model_info.get('purpose', 'Not specified')}",
                f"Processing methods: {model_info.get('methods', 'Not specified')}",
                f"Retention period: {model_info.get('retention', 'Not specified')}"
            ],
            "Model Information": [
                f"Model type: {model_info.get('model_type', 'Not specified')}",
                f"Training date: {model_info.get('training_date', 'Not specified')}",
                f"Performance metrics: {model_info.get('metrics', 'Not specified')}"
            ],
            "Limitations": [
                f"Known biases: {model_info.get('biases', 'Not specified')}",
                f"Constraints: {model_info.get('constraints', 'Not specified')}",
                f"Not suitable for: {model_info.get('exclusions', 'Not specified')}"
            ]
        }
        
        for section, items in sections.items():
            print(f"\n{section}:")
            for item in items:
                print(f"  • {item}")
        
        print("\n✓ Benefits of Transparency:")
        print("  • Builds user trust")
        print("  • Enables accountability")
        print("  • Facilitates auditing")
        print("  • Supports informed consent")
        print("  • Helps identify issues early")

transparency = TransparencyFramework()

model_documentation = {
    "sources": "Public datasets, user-contributed content",
    "period": "2020-2024",
    "volume": "10 million samples",
    "purpose": "Customer service chatbot",
    "methods": "NLP, sentiment analysis",
    "retention": "5 years",
    "model_type": "Large Language Model",
    "training_date": "January 2024",
    "metrics": "85% accuracy, 90% user satisfaction",
    "biases": "Potential bias toward English-language content",
    "constraints": "May struggle with technical jargon",
    "exclusions": "Medical diagnosis, legal advice"
}

transparency.create_data_transparency_report(model_documentation)

# =============================================================================
# SOCIETAL IMPACT ASSESSMENT
# =============================================================================

print("\n\n" + "=" * 60)
print("SOCIETAL IMPACT ASSESSMENT")
print("=" * 60)

class SocietalImpactAssessment:
    """
    This principle aims to understand a model's potential effects on society.
    
    Before deployment, consider:
    - Who will be affected?
    - What are the potential harms?
    - What are the benefits?
    - Are there disparate impacts on different groups?
    """
    
    def conduct_impact_assessment(self, ai_system):
        """
        Systematic assessment of societal impact
        """
        print(f"\n🌍 SOCIETAL IMPACT ASSESSMENT")
        print("-" * 50)
        print(f"AI System: {ai_system['name']}")
        print(f"Purpose: {ai_system['purpose']}")
        print()
        
        # Stakeholder analysis
        print("Stakeholder Analysis:")
        for stakeholder in ai_system.get('stakeholders', []):
            print(f"  • {stakeholder}")
        print()
        
        # Potential impacts
        print("Potential Positive Impacts:")
        for impact in ai_system.get('positive_impacts', []):
            print(f"  ✓ {impact}")
        print()
        
        print("Potential Negative Impacts:")
        for impact in ai_system.get('negative_impacts', []):
            print(f"  ⚠️  {impact}")
        print()
        
        # Mitigation strategies
        print("Mitigation Strategies:")
        for strategy in ai_system.get('mitigations', []):
            print(f"  → {strategy}")
        print()
        
        # Assessment questions
        print("Key Assessment Questions:")
        questions = [
            "Does it disproportionately affect vulnerable groups?",
            "Could it reinforce existing inequalities?",
            "Are there alternative approaches with less risk?",
            "How will we monitor long-term effects?",
            "Is there a process for redress if harm occurs?"
        ]
        for q in questions:
            print(f"  ? {q}")

impact_assessor = SocietalImpactAssessment()

# Example: Hiring AI system
hiring_ai = {
    "name": "Automated Resume Screening System",
    "purpose": "Screen job applications for large corporation",
    "stakeholders": [
        "Job applicants",
        "HR departments",
        "Current employees",
        "Diversity & inclusion teams",
        "Society at large"
    ],
    "positive_impacts": [
        "Faster processing of applications",
        "Reduced human workload",
        "Potentially more consistent evaluation",
        "Cost savings for companies"
    ],
    "negative_impacts": [
        "May perpetuate historical hiring biases",
        "Could disadvantage non-traditional candidates",
        "Lack of transparency in decisions",
        "Reduced human judgment and context",
        "Potential for systematic discrimination"
    ],
    "mitigations": [
        "Regular bias audits",
        "Human-in-the-loop review",
        "Diverse training data",
        "Explainable AI features",
        "Appeals process for rejected candidates",
        "Continuous monitoring of outcomes"
    ]
}

impact_assessor.conduct_impact_assessment(hiring_ai)

# =============================================================================
# RESPONSIBLE DATA DIMENSIONS
# =============================================================================

print("\n\n" + "=" * 60)
print("RESPONSIBLE DATA DIMENSIONS")
print("=" * 60)

class ResponsibleDataDimensions:
    """
    In responsible AI, "responsible data dimensions" refers to a holistic
    FOCUS ON THE ETHICAL COLLECTION AND USAGE of data throughout its lifecycle.
    
    This includes considering data from collection to deletion.
    """
    
    def evaluate_data_lifecycle(self):
        """
        Assess responsible practices across the data lifecycle
        """
        print(f"\n♻️  DATA LIFECYCLE - RESPONSIBLE PRACTICES")
        print("-" * 50)
        
        lifecycle_stages = {
            "1. Collection": [
                "Obtain informed consent",
                "Collect only necessary data",
                "Document data sources",
                "Ensure legal compliance",
                "Respect privacy preferences"
            ],
            "2. Storage": [
                "Implement strong security",
                "Encrypt sensitive data",
                "Control access appropriately",
                "Regular security audits",
                "Geographic considerations"
            ],
            "3. Usage": [
                "Use data for stated purposes only",
                "Avoid discriminatory applications",
                "Ensure data quality",
                "Maintain data accuracy",
                "Regular bias assessments"
            ],
            "4. Sharing": [
                "Obtain necessary permissions",
                "Anonymize when appropriate",
                "Use secure transfer methods",
                "Track data sharing",
                "Contractual protections"
            ],
            "5. Retention": [
                "Define retention periods",
                "Regular data audits",
                "Update outdated information",
                "Archive appropriately",
                "Document decisions"
            ],
            "6. Deletion": [
                "Honor deletion requests",
                "Secure deletion methods",
                "Remove from backups",
                "Notify relevant parties",
                "Maintain deletion logs"
            ]
        }
        
        for stage, practices in lifecycle_stages.items():
            print(f"\n{stage}")
            for practice in practices:
                print(f"  ✓ {practice}")
        
        print("\n💡 Key Principle:")
        print("Ethical considerations apply at EVERY stage of the data lifecycle,")
        print("not just at collection or model training.")

responsible_data = ResponsibleDataDimensions()
responsible_data.evaluate_data_lifecycle()

# =============================================================================
# PRACTICAL IMPLEMENTATION CHECKLIST
# =============================================================================

print("\n\n" + "=" * 60)
print("RESPONSIBLE AI IMPLEMENTATION CHECKLIST")
print("=" * 60)

checklist = {
    "Data Quality": [
        "☐ Diverse and representative training data",
        "☐ Regular bias audits",
        "☐ Data quality validation",
        "☐ Documentation of limitations"
    ],
    "Transparency": [
        "☐ Clear documentation of AI capabilities",
        "☐ Explanation of how decisions are made",
        "☐ Disclosure of data sources",
        "☐ Communication of limitations"
    ],
    "Accountability": [
        "☐ Designated responsible parties",
        "☐ Audit trails and logging",
        "☐ Regular performance monitoring",
        "☐ Incident response procedures"
    ],
    "Fairness": [
        "☐ Bias testing across demographics",
        "☐ Fairness metrics defined",
        "☐ Disparate impact analysis",
        "☐ Remediation plans"
    ],
    "Safety": [
        "☐ Harmful content filtering",
        "☐ Safety testing protocols",
        "☐ Human oversight mechanisms",
        "☐ Fail-safe procedures"
    ],
    "Privacy": [
        "☐ Privacy impact assessment",
        "☐ Data minimization",
        "☐ Consent mechanisms",
        "☐ Right to deletion"
    ]
}

print("\nBefore deploying an AI system, verify:\n")
for category, items in checklist.items():
    print(f"{category}:")
    for item in items:
        print(f"  {item}")
    print()

# =============================================================================
# KEY TAKEAWAYS
# =============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
Primary Source of Bias:
  • Quality and composition of training data
  • Underrepresented groups lead to biased outputs

Primary Ethical Concern:
  • Generation of biased or harmful content
  • Discriminatory, offensive, or false outputs

Solution - Diverse Data:
  • Use diverse and well-selected training data
  • Include multiple perspectives and demographics
  • Regular validation and auditing

Key Challenge:
  • Accessing high-quality, unbiased data
  • Data quality dimensions: accuracy, completeness, etc.

Transparency:
  • Essential for trust and accountability
  • Document data sources, methods, limitations
  • Enable informed consent and auditing

Societal Impact Assessment:
  • Understand potential effects on society
  • Consider stakeholders and vulnerable groups
  • Plan mitigation strategies

Responsible Data Dimensions:
  • Holistic focus on ethical data practices
  • Applies throughout entire data lifecycle
  • From collection to deletion

Remember: Responsible AI is not a one-time effort
It requires continuous monitoring, assessment, and improvement.
""")