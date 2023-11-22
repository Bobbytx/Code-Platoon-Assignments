import NavBar from './pages/NavBar'; // Adjust the path as per your structure
//import outlet to connect children to app
import { Outlet } from 'react-router-dom';
import './App.css'


//create function here for favorites for something, check class code

function App() {
  const [favorites, setFavorites] = useState ([])

  useEffect(() =>{
    console.log(favorites)
  }, [favorites])

  return (
    <div>
        <NavBar />
        <Outlet context= {{favorites, setFavorites}}/>
    </div>
  );
}

export default App;
