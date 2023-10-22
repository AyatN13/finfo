import SwiftUI

struct ContentView: View {
    @State private var pythonOutput: String = ""
    
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
            Text(pythonOutput)
        }
        .onAppear {
            runPythonScript()
        }
        .padding()
    }
    
    func runPythonScript() {
        let task = Process()
        task.launchPath = "/usr/bin/python3" // Set the path to your Python interpreter
        task.arguments = ["backend.py"] // Assumes that backend.py is in the same directory
        
        let pipe = Pipe()
        task.standardOutput = pipe
        
        task.launch()
        
        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        if let output = String(data: data, encoding: .utf8) {
            pythonOutput = output
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
