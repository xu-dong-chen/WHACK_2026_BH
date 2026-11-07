import { useState } from 'react'
import './App.css'

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
	const onFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    if (!file.name.toLowerCase().endsWith(".pgn")){
      alert("Please select an image file");
      return;
    }
		setSelectedFile(file);
	};
	const onFileUpload = () => {
		const formData = new FormData();
		formData.append(
			"myFile",
			selectedFile,
			selectedFile.name
		);
		console.log(selectedFile);
		axios.post("api/uploadfile", formData);
	};
	const fileData = () => {
		if (selectedFile) {
			return (
				<div>
					<h2>File Details:</h2>
					<p>File Name: {selectedFile.name}</p>
					<p>File Type: {selectedFile.type}</p>
					<p>
						Last Modified: {selectedFile.lastModifiedDate.toDateString()}
					</p>
				</div>
			);
		} else {
			return (
				<div>
					<br />
					<h4>Choose before Pressing the Upload button</h4>
				</div>
			);
		}
	};


  return (
    <div>
    <div className='dataset'>
				<input type="file" accept=".pgn" onChange={onFileChange} />
				<button onClick={onFileUpload}>Upload</button>
		</div>
	{fileData()}
  </div>
  );
}

export default App
