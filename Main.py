import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AvrSs11xEdFWZOuEsI_DogV_AGyg1_uA-2m8sCJVnWv4PSdyS0Pr9MXPbOksAj3W0NIlAfRd0RYG5JBqxENIwM3BFDPMH8SVG5QOJtc13k-T0-tSPzc5d6m6y7o67lhvHVj3bCo'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
