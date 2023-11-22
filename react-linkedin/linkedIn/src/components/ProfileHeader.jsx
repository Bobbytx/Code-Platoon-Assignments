import ProfilePhoto from './ProfilePhoto';
import ProfileInfo from './ProfileInfo';
import CoverPhoto from './CoverPhoto';

const ProfileHeader = () => {
    return (
        <div className="profile-header">
            <div className="cover-photo">
                <CoverPhoto />
            </div>
            <div className="profile-photo">
                <ProfilePhoto />
            </div>
            <div className="profile-info">
                <ProfileInfo />
            </div>
            <div className="followButton">
                <button>Follow</button>
            </div>
        </div>
    );
};

export default ProfileHeader;