export default function InfoSection() {
  return (
    <section className="mt-12 pt-8 border-t-2 border-gray-200">
      <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">How It Works</h2>
      
      <div className="grid md:grid-cols-3 gap-6">
        <div className="text-center p-6 bg-gray-50 rounded-xl">
          <div className="w-16 h-16 bg-primary text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
            1
          </div>
          <h3 className="text-xl font-semibold mb-2">Upload Photo</h3>
          <p className="text-gray-600">Take a photo of your waste item</p>
        </div>

        <div className="text-center p-6 bg-gray-50 rounded-xl">
          <div className="w-16 h-16 bg-primary text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
            2
          </div>
          <h3 className="text-xl font-semibold mb-2">AI Analysis</h3>
          <p className="text-gray-600">Three specialized agents analyze it</p>
        </div>

        <div className="text-center p-6 bg-gray-50 rounded-xl">
          <div className="w-16 h-16 bg-primary text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto mb-4">
            3
          </div>
          <h3 className="text-xl font-semibold mb-2">Get Guidance</h3>
          <p className="text-gray-600">Receive disposal and upcycling advice</p>
        </div>
      </div>
    </section>
  )
}
