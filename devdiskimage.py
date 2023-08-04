from developer_disk_image.repo import DeveloperDiskImageRepository

repo = DeveloperDiskImageRepository.create()

# will get both the APFS and the signature file
developer_disk_image = repo.get_developer_disk_image('16.4')

# will get all necessary files for mount
personalized_disk_image = repo.get_personalized_disk_image()