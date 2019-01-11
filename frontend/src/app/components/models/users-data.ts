declare namespace UserData {

  interface SimpleUser {
    id: string,
    username: string,
    email: string,
    telephone: number,
    profile_img: string,
    profile_url: string
  }

  interface Client extends SimpleUser {
  }

  interface Trainer extends SimpleUser {

  }
}
