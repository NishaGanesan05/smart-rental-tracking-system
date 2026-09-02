import { useEffect, useState } from 'react'
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer
} from 'recharts'

const STATUS_COLORS = {
  ACTIVE: '#FFCD11',
  AVAILABLE: '#2E7D32',
  UNASSIGNED: '#3A3A3A',
  RENTED: '#FFCD11',
  OVERDUE: '#C62828',
  RETURNED: '#7A7F83'
}

function AssetStatusChart() {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/assets/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch assets')
        }

        return response.json()
      })
      .then((assets) => {
        const statusCounts = {}

        assets.forEach((asset) => {
          statusCounts[asset.status] =
            (statusCounts[asset.status] || 0) + 1
        })

        const chartData = Object.entries(statusCounts).map(
          ([status, count]) => ({
            name: status,
            value: count
          })
        )

        setData(chartData)
        setLoading(false)
      })
      .catch((error) => {
        console.error('Error fetching asset status:', error)
        setLoading(false)
      })
  }, [])

  if (loading) {
    return (
      <div className="chart-state">
        Loading asset analytics...
      </div>
    )
  }

  if (data.length === 0) {
    return (
      <div className="chart-state">
        No asset status data available.
      </div>
    )
  }

  return (
    <div className="analytics-chart">

      <ResponsiveContainer width="100%" height={330}>

        <PieChart>

          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            cx="50%"
            cy="48%"
            outerRadius={105}
            innerRadius={58}
            paddingAngle={3}
            stroke="#ffffff"
            strokeWidth={3}
            labelLine={false}
            label={({ name, percent }) =>
              `${name} ${(percent * 100).toFixed(0)}%`
            }
          >

            {data.map((entry) => (
              <Cell
                key={entry.name}
                fill={
                  STATUS_COLORS[entry.name] || '#9EA2A5'
                }
              />
            ))}

          </Pie>

          <Tooltip
            contentStyle={{
              borderRadius: '6px',
              border: '1px solid #E1E3E5',
              boxShadow: '0 4px 14px rgba(0, 0, 0, 0.12)',
              fontSize: '12px'
            }}
          />

          <Legend
            verticalAlign="bottom"
            height={36}
            iconType="circle"
          />

        </PieChart>

      </ResponsiveContainer>

    </div>
  )
}

export default AssetStatusChart