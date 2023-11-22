import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import CharactersPage from "./pages/CharacterPage";
import CharacterDetailsPage from "./pages/CharacterDetailsPage";
import NotFoundPage from "./pages/NotFoundPage";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        //App has children, this is an array
        children: [
            {
                //always true or false
                index: true,
                element: <HomePage />,
            },
            {
                path: 'about/',
                element: <AboutPage />,
            },
            {
                path: 'characters/',
                element: <CharactersPage />,
            },
            {
                path: 'characters/:id',
                element: <CharacterDetailsPage />,
            },
            {
                path: 'favorites/',
                element: <FavoritesPage />
            }
        ],
        errorElement: <NotFoundPage />
    }
])

export default router;