import { useState, useEffect } from 'react'
import UploadSection from './components/UploadSection'
import ResultsSection from './components/ResultsSection'
import InfoSection from './components/InfoSection'

const API_BASE = import.meta.env.PROD ? '' : ''

function App() {
  const [selectedFile, setSelectedFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [results, setResults] = useState(null)
  const [apiConfigured, setApiConfigured] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${API_BASE}/health`)
      .then(res => res.json())
      .then(data => setApiConfigured(data.api_configured))
      .catch(err => console.error('Health check failed:', err))
  }, [])

  const handleAnalyze = async () => {
    if (!selectedFile) return

    setLoading(true)
    setResults(null)
    setError(null)

    const formData = new FormData()
    formData.append('file', selectedFile)

    try {
      const response = await fetch(`${API_BASE}/api/analyze`, {
        method: 'POST',
        body: formData
      })

      if (!response.ok) {
        const error = await response.json()
        throw new Error(error.error || 'Analysis failed')
      }

      const data = await response.json()
      setResults(data)
    } catch (error) {
      setError(error.message || 'Something went wrong. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = async () => {
    if (!results) return

    try {
      const response = await fetch(`${API_BASE}/api/export/${results.analysis_id}?format=markdown`)
      const data = await response.json()
      
      const blob = new Blob([data.content], { type: 'text/markdown' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `ecolens-analysis-${results.analysis_id}.md`
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
    } catch (error) {
      alert('Error downloading report')
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 via-purple-700 to-indigo-800">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        <header className="text-center text-white mb-12">
          <h1 className="text-5xl font-bold mb-2">♻️ EcoLens</h1>
          <p className="text-xl opacity-90">The Intelligent Waste Analyst</p>
          {!apiConfigured && (
            <div className="mt-4 bg-yellow-500 text-black px-4 py-2 rounded-lg inline-block">
              ⚠️ API key not configured
            </div>
          )}
        </header>

        <main className="bg-white rounded-2xl shadow-2xl p-8">
          <UploadSection
            selectedFile={selectedFile}
            setSelectedFile={setSelectedFile}
            onAnalyze={handleAnalyze}
            loading={loading}
          />

          {results && (
            <ResultsSection
              results={results}
              onDownload={handleDownload}
            />
          )}

          <InfoSection />
        </main>

        <footer className="text-center text-white mt-8">
          <p>&copy; 2026 EcoLens. Making sustainable choices easy.</p>
          <div className="mt-2 space-x-4">
            <a href="/docs" className="hover:underline">API Docs</a>
            <a href="/redoc" className="hover:underline">ReDoc</a>
          </div>
        </footer>
      </div>

      {loading && (
        <div className="fixed inset-0 bg-black bg-opacity-80 flex flex-col items-center justify-center z-50">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-primary"></div>
          <p className="text-white mt-4 text-lg">Analyzing your waste item...</p>
        </div>
      )}

      {error && (
        <div className="fixed inset-0 bg-black bg-opacity-60 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl p-8 max-w-md w-full shadow-2xl">
            <div className="text-center">
              <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-gray-800 mb-2">Oops!</h3>
              <p className="text-gray-600 mb-6">{error}</p>
              <div className="space-y-2">
                <button
                  onClick={() => setError(null)}
                  className="w-full bg-primary text-white py-3 px-6 rounded-xl font-semibold hover:bg-green-700 transition-colors"
                >
                  Try Again
                </button>
                {error.includes('high demand') && (
                  <p className="text-sm text-gray-500">The AI is busy. Please wait a moment.</p>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App
