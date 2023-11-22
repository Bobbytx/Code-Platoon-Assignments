import AboutMe from './AboutMe';
import ProfileHeader from './ProfileHeader';
import Education from './Education';
import JobHistory from './JobHistory';

const LinkedInProfile = () => {
    return (
        <div className="centerAll">
        <ProfileHeader />
        <AboutMe />
        <JobHistory />
        <Education />
        </div>
    );
}

export default LinkedInProfile;