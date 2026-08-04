"""
This file demonstrates the use of the Exposure class
for estimating astrophotography Signal-to-Noise Ratio.
"""

from optics_set_class import Exposure


def main():

    exposure = Exposure(
        exposure_time=60,
        iso=800,
        aperture=2.8,
        focal_length=300,
        read_noise=3.2,
        dark_current=0.01,
    )

    # --------------------------------------------------
    # Example target
    # --------------------------------------------------

    object_flux = 20.0      # electrons/sec

    sky_flux = 8.0          # electrons/sec

    snr = exposure.signal_to_noise_estimate(
        object_flux,
        sky_flux,
    )

    print(exposure)

    print(f"Entrance pupil : {exposure.entrance_pupil:.1f} mm")

    print(f"Collecting area: {exposure.collecting_area:.0f} mm²")

    print(f"Estimated SNR  : {snr:.2f}")


if __name__ == "__main__":
    main()