export default function ResultsSection({ results, onDownload }) {
  return (
    <section className="mb-8">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Analysis Results</h2>
      
      <div className="grid md:grid-cols-3 gap-6 mb-6">
        <div className="bg-gray-50 rounded-xl p-6">
          <h3 className="text-lg font-semibold text-primary mb-3">🔬 Material Analysis</h3>
          <p className="text-gray-700 whitespace-pre-wrap">{results.material_analysis}</p>
        </div>

        <div className="bg-gray-50 rounded-xl p-6">
          <h3 className="text-lg font-semibold text-primary mb-3">👮 Disposal Verdict</h3>
          <p className="text-gray-700 whitespace-pre-wrap">{results.verdict}</p>
        </div>

        <div className="bg-gray-50 rounded-xl p-6">
          <h3 className="text-lg font-semibold text-primary mb-3">🎨 Upcycling Ideas</h3>
          <p className="text-gray-700 whitespace-pre-wrap">{results.upcycling_ideas}</p>
        </div>
      </div>

      <button
        onClick={onDownload}
        className="w-full bg-secondary text-white py-3 px-6 rounded-xl text-lg font-semibold hover:bg-blue-600 transition-colors"
      >
        Download Report
      </button>
    </section>
  )
}
