import { useState } from 'react'
import './App.css'

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [results,setResults] = useState([])
	const onFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    if (!file.name.toLowerCase().endsWith(".pgn")){
      alert("Please select an PGN file");
      return;
    }
		setSelectedFile(file);
	};
	const onFileUpload = async () => {
		if (!selectedFile){
			alert("Please select a PGN file first");
			return;
		}

		const formData = new FormData();
		formData.append("file", selectedFile);

		try{
			const response = await fetch("http://127.0.0.1:8000/upload-file", {
										method: "POST",
										body: formData
									});

			alert("File uploaded")

			const data = await response.json();
			setResults(data.results);
		} catch (error){
			console.error(error)
			alert("Error with uploading the file")
		}
	};


  return (
	<div className="app-layout">

        {/* LEFT SIDEBAR */}
        <aside className="pattern-sidebar">
            <h2>Top Patterns</h2>

            {results.length === 0 ? (
                <p>No patterns found yet.</p>
            ) : (
                results.map((item, index) => (
                    <div className="pattern-entry" key={index}>
                        <h4>Pattern #{index + 1}</h4>

                        <p>
                            {JSON.stringify(item.pattern)}
                        </p>

                        <p>
                            Win rate: {(item.win_rate * 100).toFixed(2)}%
                        </p>
                    </div>
                ))
            )}
        </aside>

		<div className='uploading'>
			<h2>Upload PGN Files</h2>
			<div className='dataset'>
				<input type="file" accept=".pgn" onChange={onFileChange} />
				<button onClick={onFileUpload}>Upload</button>
			</div>
		</div>
		
  	</div>
  );
}

export default App
