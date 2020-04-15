import enum


class ErrorMessages(enum.Enum):
    noMatch = "No such email exists"
    samePassword = "New password cannot be same as old password"
    passwordChange = "Your password has been change successfully"
    notValid = "Invalid data sent"
    invalidCode = "Your reset code is invalid"
    expired = "Your reset code has expired"
