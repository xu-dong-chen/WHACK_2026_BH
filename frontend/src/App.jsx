import { useState } from 'react'
import './App.css'

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
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
		} catch (error){
			console.error(error)
			alert("Error with uploading the file")
		}
	};


  return (
    <div>
    	<div className='dataset'>
			<input type="file" accept=".pgn" onChange={onFileChange} />
			<button onClick={onFileUpload}>Upload</button>
		</div>

		<h1>Top Patterns Found</h1>
		
  	</div>
  );
}

export default App
