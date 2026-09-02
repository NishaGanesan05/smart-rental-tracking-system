import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'

function RecommendationCard() {
  const [recommendation, setRecommendation] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/recommendations/open')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch recommendations')
        }

        return response.json()
      })
      .then((data) => {
        if (!Array.isArray(data) || data.length === 0) {
          setRecommendation(null)
          setLoading(false)
          return
        }

        const priorityRank = {
          HIGH: 1,
          MEDIUM: 2,
          LOW: 3
        }

        const sortedRecommendations = [...data].sort(
          (a, b) =>
            (priorityRank[a.priority] || 99) -
            (priorityRank[b.priority] || 99)
        )

        setRecommendation(sortedRecommendations[0])
        setLoading(false)
      })
      .catch((error) => {
        console.error(
          'Error fetching recommendations:',
          error
        )

        setError('Unable to load recommendation.')
        setLoading(false)
      })
  }, [])

  return (
    <section className="recommendation-card">

      <div className="recommendation-header">

        <div className="recommendation-title">

          <div className="recommendation-icon">
            ✦
          </div>

          <div>
            <p className="recommendation-eyebrow">
              AI-POWERED INSIGHT
            </p>

            <h2>
              Recommended Action
            </h2>
          </div>

        </div>

        {recommendation && (
          <span
            className={`recommendation-priority ${
              recommendation.priority.toLowerCase()
            }`}
          >
            {recommendation.priority} PRIORITY
          </span>
        )}

      </div>


      {loading && (
        <div className="recommendation-state">
          Analyzing fleet activity...
        </div>
      )}


      {!loading && error && (
        <div className="recommendation-state">
          {error}
        </div>
      )}


      {!loading &&
        !error &&
        !recommendation && (
          <div className="recommendation-state">
            No active recommendations at this time.
          </div>
        )}


      {!loading &&
        !error &&
        recommendation && (

          <div className="recommendation-content">

            <div className="recommendation-main">

              <span className="recommendation-type">
                {recommendation.recommendation_type.replaceAll(
                  '_',
                  ' '
                )}
              </span>

              <h3>
                {recommendation.message}
              </h3>

              <p>
                {recommendation.reason}
              </p>

            </div>


            <div className="recommendation-meta">

              <div className="recommendation-asset">

                <span>
                  ASSET
                </span>

                <strong>
                  {recommendation.asset_id}
                </strong>

              </div>


              <Link
                className="recommendation-button"
                to="/recommendations"
              >
                View Recommendations
                <span>→</span>
              </Link>

            </div>

          </div>

        )}

    </section>
  )
}

export default RecommendationCard