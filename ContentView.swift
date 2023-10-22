import SwiftUI

struct ContentView: View {
    @State private var stockInfo: [Stock] = []
    
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Stock Information")
            List(stockInfo, id: \.ticker) { stock in
                VStack(alignment: .leading) {
                    Text(stock.name).bold()
                    Text("Current Price: \(stock.currentPrice)")
                    Text("Market Cap: \(stock.marketCap)")
                    // Add more fields as required
                }
            }
        }
        .onAppear(perform: loadStockData)
        .padding()
    }
    
    func loadStockData() {
        // Ensure Python was initialized correctly
        guard let python = try? Python.attemptImport("sys") else {
            print("Failed to initialize Python")
            return
        }
        
        // Since backend.py is in the same directory, we use the following to get the directory path
        let dir = Bundle.main.bundlePath
        
        // Add the directory containing your script to the Python sys.path
        python.sys.path.append(dir)
        
        // Import your Python script
        guard let backend = try? Python.attemptImport("backend") else {
            print("Failed to import backend.py")
            return
        }
        
        // Execute the main function
        let resultJSON = String(backend.main()) ?? ""
        if let data = resultJSON.data(using: .utf8),
           let decodedData = try? JSONDecoder().decode([Stock].self, from: data) {
            stockInfo = decodedData
        }
    }
}

struct Stock: Decodable {
    let ticker: String
    let name: String
    let currentPrice: Double
    let marketCap: Double
    // Add more fields as required based on your Python script's output
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

