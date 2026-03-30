import { useRef } from 'react'

export default function UploadSection({ selectedFile, setSelectedFile, onAnalyze, loading }) {
  const fileInputRef = useRef(null)

  const handleFileSelect = (file) => {
    const validTypes = ['image/jpeg', 'image/png', 'image/gif']
    if (!validTypes.includes(file.type)) {
      alert('Please upload a JPEG, PNG, or GIF image')
      return
    }

    if (file.size > 20 * 1024 * 1024) {
      alert('File size must be less than 20MB')
      return
    }

    setSelectedFile(file)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    const file = e.dataTransfer.files[0]
    if (file) handleFileSelect(file)
  }

  const handleDragOver = (e) => {
    e.preventDefault()
  }

  return (
    <section className="mb-8">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Analyze Your Waste Item</h2>
      
      <div
        onClick={() => fileInputRef.current?.click()}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        className="border-4 border-dashed border-primary rounded-xl p-12 text-center cursor-pointer hover:bg-green-50 transition-colors bg-gray-50"
      >
        <input
          ref={fileInputRef}
          type="file"
          accept="image/*"
          onChange={(e) => handleFileSelect(e.target.files[0])}
          className="hidden"
        />
        
        {selectedFile ? (
          <div className="space-y-2">
            <svg className="w-16 h-16 mx-auto text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <p className="text-lg font-semibold">{selectedFile.name}</p>
            <p className="text-gray-600">{(selectedFile.size / 1024 / 1024).toFixed(2)} MB</p>
          </div>
        ) : (
          <div className="space-y-2">
            <svg className="w-16 h-16 mx-auto text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
            </svg>
            <p className="text-lg">Click to upload or drag and drop</p>
            <p className="text-sm text-gray-500">JPEG, PNG, GIF (max 20MB)</p>
          </div>
        )}
      </div>

      <button
        onClick={onAnalyze}
        disabled={!selectedFile || loading}
        className="mt-4 w-full bg-primary text-white py-3 px-6 rounded-xl text-lg font-semibold hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
      >
        {loading ? 'Analyzing...' : 'Analyze with EcoLens'}
      </button>
    </section>
  )
}
