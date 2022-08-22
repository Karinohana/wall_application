import React from "react";

export const Sidebar = () => {
  return (
    <div class="profile-section-user">
      <div class="profile-cover-img">
        <img
          src="https://bootdey.com/img/Content/flores-amarillas-wallpaper.jpeg"
          alt=""
        ></img>
      </div>
      <div class="profile-info-brief p-3">
        <img
          class="img-fluid user-profile-avatar"
          src="https://bootdey.com/img/Content/avatar/avatar6.png"
          alt=""
        ></img>
        <div class="text-center">
          <h5 class="text-uppercase mb-4">John Doe</h5>
          <p class="text-muted fz-base">
            I'm John Doe a web developer and software engineer. I studied
            computer science and software engineering.
          </p>
        </div>
      </div>

      <hr class="m-0"></hr>
      <div class="hidden-sm-down">
        <hr class="m-0"></hr>
        <div class="profile-info-contact p-4">
          <h6 class="mb-3">Contact Information</h6>
          <table class="table">
            <tbody>
              <tr>
                <td>
                  <strong>URL:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">Rathemes.com/inde.html</p>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>EMAIL:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">rathemes@gmail.com</p>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>PHONE:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">01145525755</p>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>SKYPE:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">Rathemes</p>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <hr class="m-0"></hr>
        <div class="profile-info-general p-4">
          <h6 class="mb-3">General Information</h6>
          <table class="table">
            <tbody>
              <tr>
                <td>
                  <strong>JOB:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">Web Developer</p>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>POSITION:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">Team Manager</p>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>STUDIED:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">Computer Science</p>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>LAST SEEN:</strong>
                </td>
                <td>
                  <p class="text-muted mb-0">Yesterday 8:00 AM</p>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <hr class="m-0"></hr>
      </div>
    </div>
  );
};
