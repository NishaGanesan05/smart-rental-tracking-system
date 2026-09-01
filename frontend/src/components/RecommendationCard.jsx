import { recommendations } from '../data/recommendations'

function RecommendationCard() {
  const recommendation = recommendations[0]

  return (
    <section className="recommendation-panel">
      <div className="recommendation-content">
        <span className="recommendation-label">
          AI RECOMMENDATION
        </span>

        <h2>{recommendation.title}</h2>

        <p>{recommendation.description}</p>
      </div>

      <button className="recommendation-button">
        View recommendation
      </button>
    </section>
  )
}

export default RecommendationCard