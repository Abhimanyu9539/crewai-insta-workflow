"""
Data models for Instagram Content Creation System
Defines all data structures used by CrewAI agents
"""
from datetime import datetime
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from enum import Enum


class ContentMode(str, Enum):
    """Content generation modes"""
    TOPIC = "topic"
    MIMIC_ACCOUNT = "mimic_account"


class BrandVoice(str, Enum):
    """Available brand voice options"""
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    INSPIRATIONAL = "inspirational"
    EDUCATIONAL = "educational"
    HUMOROUS = "humorous"
    LUXURY = "luxury"
    AUTHENTIC = "authentic"


class ContentType(str, Enum):
    """Instagram content types"""
    SINGLE_POST = "single_post"
    CAROUSEL = "carousel"
    REEL = "reel"
    STORY = "story"


class ContentLength(str, Enum):
    """Caption length preferences"""
    SHORT = "short"      # 50-150 characters
    MEDIUM = "medium"    # 150-500 characters
    LONG = "long"        # 500+ characters


class UserInput(BaseModel):
    """
    User input for content generation
    Supports both topic-based and account-mimicking modes
    """
    mode: ContentMode = Field(..., description="Generation mode: topic or mimic_account")
    
    # Topic mode inputs
    topic: Optional[str] = Field(None, description="Topic for content creation")
    
    # Account mimicking mode inputs
    target_account: Optional[str] = Field(None, description="Instagram account handle to analyze and mimic")
    
    # Common settings
    brand_voice: BrandVoice = Field(default=BrandVoice.PROFESSIONAL)
    content_type: ContentType = Field(default=ContentType.SINGLE_POST)
    content_length: ContentLength = Field(default=ContentLength.MEDIUM)
    
    # Optional customization
    target_audience: Optional[str] = Field(None, description="Target audience description")
    industry: Optional[str] = Field(None, description="Industry or niche")
    additional_context: Optional[str] = Field(None, description="Additional requirements or context")
    
    # Generation preferences
    num_variations: int = Field(default=3, description="Number of caption variations to generate")
    include_hashtags: bool = Field(default=True)
    include_emojis: bool = Field(default=True)
    
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }


class TrendData(BaseModel):
    """Individual trend item"""
    keyword: str
    volume: Optional[int] = None
    growth_rate: Optional[float] = None
    relevance_score: float = Field(ge=0.0, le=10.0)
    category: Optional[str] = None


class TrendResearch(BaseModel):
    """Output from Trend Researcher Agent"""
    # Core trend data
    trending_hashtags: List[str] = Field(default_factory=list)
    trending_topics: List[TrendData] = Field(default_factory=list)
    viral_formats: List[str] = Field(default_factory=list)
    
    # Competitive analysis
    competitor_insights: List[Dict[str, Any]] = Field(default_factory=list)
    successful_post_patterns: List[str] = Field(default_factory=list)
    
    # Cultural context
    cultural_moments: List[str] = Field(default_factory=list)
    seasonal_trends: List[str] = Field(default_factory=list)
    
    # Recommendations
    recommended_posting_times: List[str] = Field(default_factory=list)
    content_gaps: List[str] = Field(default_factory=list)
    tone_recommendations: List[str] = Field(default_factory=list)
    
    # Metadata
    trend_score: float = Field(default=0.0, ge=0.0, le=10.0)
    research_depth: str = Field(default="standard")
    research_timestamp: datetime = Field(default_factory=datetime.now)
    data_sources: List[str] = Field(default_factory=list)


class AccountMetrics(BaseModel):
    """Instagram account metrics"""
    followers: Optional[int] = None
    following: Optional[int] = None
    posts: Optional[int] = None
    engagement_rate: Optional[float] = None
    avg_likes: Optional[int] = None
    avg_comments: Optional[int] = None


class ContentPattern(BaseModel):
    """Identified content patterns from account analysis"""
    pattern_type: str  # e.g., "question_posts", "story_telling", "educational"
    frequency: float  # How often this pattern appears (0.0 to 1.0)
    example: str
    engagement_level: str  # "high", "medium", "low"


class AccountAnalysis(BaseModel):
    """Comprehensive Instagram account analysis"""
    account_handle: str
    account_name: Optional[str] = None
    bio: Optional[str] = None
    website: Optional[str] = None
    is_verified: bool = Field(default=False)
    is_business: bool = Field(default=False)
    
    # Metrics
    metrics: AccountMetrics = Field(default_factory=AccountMetrics)
    
    # Content analysis
    content_themes: List[str] = Field(default_factory=list)
    hashtag_patterns: List[str] = Field(default_factory=list)
    content_patterns: List[ContentPattern] = Field(default_factory=list)
    
    # Writing style analysis
    avg_caption_length: Optional[int] = None
    emoji_usage_frequency: Optional[float] = None
    writing_tone: List[str] = Field(default_factory=list)
    common_phrases: List[str] = Field(default_factory=list)
    
    # Posting behavior
    posting_frequency: Optional[str] = None
    optimal_posting_times: List[str] = Field(default_factory=list)
    content_type_distribution: Dict[str, float] = Field(default_factory=dict)
    
    # Sample content
    sample_captions: List[str] = Field(default_factory=list, max_items=10)
    
    # Analysis metadata
    posts_analyzed: int = Field(default=0)
    analysis_timestamp: datetime = Field(default_factory=datetime.now)
    confidence_score: float = Field(default=0.0, ge=0.0, le=10.0)


class CaptionVariation(BaseModel):
    """Individual caption variation"""
    content: str
    style: str  # e.g., "storytelling", "educational", "question-based"
    hook_strength: float = Field(ge=0.0, le=10.0)
    estimated_engagement: str = Field(default="medium")  # "low", "medium", "high"
    target_emotion: Optional[str] = None
    word_count: int = Field(default=0)
    
    # Analysis scores
    readability_score: Optional[float] = None
    sentiment_score: Optional[float] = None
    call_to_action_strength: Optional[float] = None


class HashtagSet(BaseModel):
    """Organized hashtags by category and strategy"""
    primary: List[str] = Field(default_factory=list, description="Main topic hashtags (3-5)")
    secondary: List[str] = Field(default_factory=list, description="Supporting hashtags (5-10)")
    niche: List[str] = Field(default_factory=list, description="Community-specific hashtags (3-7)")
    trending: List[str] = Field(default_factory=list, description="Currently trending hashtags (2-5)")
    branded: List[str] = Field(default_factory=list, description="Brand-specific hashtags (1-3)")
    
    total_count: int = Field(default=0)
    estimated_reach: Dict[str, str] = Field(default_factory=dict)


class CreativeContent(BaseModel):
    """Output from Creative Writer Agent"""
    # Main content variations
    caption_variations: List[CaptionVariation] = Field(default_factory=list)
    
    # Specialized content
    carousel_slides: Optional[List[Dict[str, str]]] = None
    story_content: Optional[List[str]] = None
    
    # Engagement elements
    call_to_action_options: List[str] = Field(default_factory=list)
    question_prompts: List[str] = Field(default_factory=list)
    
    # Content strategy
    content_series_ideas: List[str] = Field(default_factory=list)
    repurposing_suggestions: List[str] = Field(default_factory=list)
    
    # Metadata
    generation_approach: str = Field(default="standard")
    inspiration_source: Optional[str] = None  # topic or account handle
    generation_timestamp: datetime = Field(default_factory=datetime.now)


class PerformancePrediction(BaseModel):
    """AI-powered performance predictions"""
    # Engagement predictions
    predicted_likes_range: str = Field(default="medium")
    predicted_comments_range: str = Field(default="medium") 
    predicted_shares_range: str = Field(default="low")
    predicted_saves_range: str = Field(default="medium")
    
    # Scoring
    viral_potential: float = Field(ge=0.0, le=10.0, default=5.0)
    engagement_potential: float = Field(ge=0.0, le=10.0, default=5.0)
    brand_alignment: float = Field(ge=0.0, le=10.0, default=5.0)
    trend_relevance: float = Field(ge=0.0, le=10.0, default=5.0)
    
    # Timing recommendations
    best_posting_time: Optional[str] = None
    best_posting_day: Optional[str] = None
    
    # Audience insights
    target_reach_estimate: Optional[str] = None
    audience_resonance_factors: List[str] = Field(default_factory=list)


class FinalPost(BaseModel):
    """Final optimized Instagram post ready for publishing"""
    # Core content
    caption: str
    hashtags: HashtagSet
    content_type: ContentType
    
    # Performance data
    performance_prediction: PerformancePrediction
    
    # Visual recommendations
    visual_suggestions: Dict[str, Any] = Field(default_factory=dict)
    
    # Accessibility & compliance
    alt_text_suggestion: Optional[str] = None
    accessibility_notes: List[str] = Field(default_factory=list)
    compliance_check: bool = Field(default=True)
    content_warnings: List[str] = Field(default_factory=list)
    
    # Metadata
    generation_mode: ContentMode
    source: str  # topic or account handle
    brand_voice: BrandVoice
    selected_variation_index: int = Field(default=0)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    estimated_publish_time: Optional[datetime] = None


class GenerationResult(BaseModel):
    """Complete result from the content generation pipeline"""
    # Input
    user_input: UserInput
    
    # Agent outputs
    trend_research: Optional[TrendResearch] = None
    account_analysis: Optional[AccountAnalysis] = None
    creative_content: CreativeContent
    
    # Final outputs
    final_posts: List[FinalPost] = Field(default_factory=list)
    recommended_post: Optional[FinalPost] = None
    
    # Pipeline metadata
    generation_time_seconds: Optional[float] = None
    agents_used: List[str] = Field(default_factory=list)
    success: bool = Field(default=True)
    error_messages: List[str] = Field(default_factory=list)
    
    # Quality metrics
    overall_quality_score: float = Field(default=0.0, ge=0.0, le=10.0)
    diversity_score: float = Field(default=0.0, ge=0.0, le=10.0)
    
    created_at: datetime = Field(default_factory=datetime.now)


# Utility functions for model validation and conversion
def validate_instagram_handle(handle: str) -> str:
    """Validate and clean Instagram handle"""
    if handle.startswith('@'):
        handle = handle[1:]
    if not handle.replace('_', '').replace('.', '').isalnum():
        raise ValueError("Invalid Instagram handle format")
    return handle.lower()


def estimate_reading_time(text: str) -> int:
    """Estimate reading time in seconds (average 200 words per minute)"""
    word_count = len(text.split())
    return max(1, int((word_count / 200) * 60))


def calculate_engagement_score(likes: int, comments: int, shares: int, followers: int) -> float:
    """Calculate engagement rate percentage"""
    if followers == 0:
        return 0.0
    total_engagement = likes + (comments * 3) + (shares * 5)  # Weighted engagement
    return min(100.0, (total_engagement / followers) * 100)