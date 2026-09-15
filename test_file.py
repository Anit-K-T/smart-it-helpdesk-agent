def password_help(user_id=None):
    print("\n[IT TOOL: PASSWORD HELPER]")

    # Get the user record from memory
    user_record = get_user(user_id)

    if not user_record:
        print("-> User record not found.")
        return False

    print(
        f"-> Welcome, {user_record['name']}. "
        "Initiating verification protocol..."
    )

    # ========================================================
    # ATTEMPT 1: SECURITY QUESTIONS
    # ========================================================

    print("\n----Attempt 1 of 2----")
    print("\n[Attempt 1: Security Verification]")

    dob_input = input(
        "Enter your Date of Birth (YYYY-MM-DD): "
    ).strip()

    color_input = input(
        "Enter your Favorite Color: "
    ).strip().capitalize()

    place_input = input(
        "Enter your Birthplace / Hometown: "
    ).strip().capitalize()

    questions_correct = (
        dob_input == user_record.get("dob") and
        color_input == user_record.get(
            "fav_color", ""
        ).capitalize() and
        place_input == user_record.get(
            "place", ""
        ).capitalize()
    )

    # ========================================================
    # SECURITY VERIFICATION SUCCESS
    # ========================================================

    if questions_correct:

        print(
            "\n-> Security verification passed successfully!"
        )

        # Generate temporary password
        temp_pass = (
            "TempPass#"
            + "".join(
                random.choices(
                    string.digits,
                    k=4
                )
            )
        )

        print(
            f"-> Temporary password generated: {temp_pass}"
        )

        # Store temporary password in memory.json
        update_user(
            user_id,
            {
                "temporary_password": temp_pass
            }
        )

        success = input(
            "Were you able to log in with this temporary password? "
            "(yes/no): "
        ).strip().lower()

        if success == "yes":
            return True

        print(
            "-> Attempt 1 failed to resolve the issue."
        )

    else:

        print(
            "-> Verification failed: One or more security "
            "answers do not match company records."
        )

    # ========================================================
    # ATTEMPT 2: OTP FALLBACK
    # ========================================================

    print("\n----Attempt 2 of 2----")
    print("\n[Attempt 2: OTP Fallback Protocol]")

    print(
        "-> Generating One-Time Password (OTP)..."
    )

    input(
        "Enter your registered email to receive the OTP "
        "(simulated): "
    )

    # Generate 4-digit OTP
    otp_code = "".join(
        random.choices(
            string.digits,
            k=4
        )
    )

    # Store OTP in memory.json
    update_user(
        user_id,
        {
            "otp": otp_code
        }
    )

    # Display OTP for demonstration
    print(
        f"-> [SIMULATED OTP]: {otp_code}"
    )

    otp_input = input(
        "Please enter the OTP provided by the system: "
    ).strip()

    # ========================================================
    # OTP VERIFICATION
    # ========================================================

    if otp_code == otp_input:

        print(
            "-> OTP verified successfully!"
        )

        # Generate temporary password
        temp_pass = (
            "TempPass#"
            + "".join(
                random.choices(
                    string.digits,
                    k=4
                )
            )
        )

        print(
            f"-> Temporary password generated: {temp_pass}"
        )

        # Store temporary password in memory.json
        update_user(
            user_id,
            {
                "temporary_password": temp_pass
            }
        )

        success = input(
            "Were you able to log in with this temporary password? "
            "(yes/no): "
        ).strip().lower()

        if success == "yes":
            return True

        print(
            "-> Attempt 2 failed to resolve the issue."
        )

        return False

    else:

        print(
            "-> Error: Invalid OTP entered."
        )

        return False

