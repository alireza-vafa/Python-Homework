import math

class Exposure:
    """
    Parameters
    ----------
    exposure_time : float
        Exposure duration [s]

    iso : int
        Camera ISO value.
        (Currently stored only for reference.)

    aperture : float
        Lens f-number.

    focal_length : float
        Lens focal length [mm]

    read_noise : float
        Camera read noise [electrons RMS]

    dark_current : float
        Dark current [electrons/pixel/second]
    """

    def __init__(
        self,
        exposure_time,
        iso,
        aperture,
        focal_length,
        read_noise,
        dark_current,
    ):

        self.exposure_time = exposure_time
        self.iso = iso
        self.aperture = aperture
        self.focal_length = focal_length

        self.read_noise = read_noise
        self.dark_current = dark_current

    # ------------------------------------------------------

    @property
    def entrance_pupil(self):
        """
        Lens entrance pupil diameter [mm].

        D = f / N
        """

        return self.focal_length / self.aperture

    # ------------------------------------------------------

    @property
    def collecting_area(self):
        """
        Optical collecting area [mm²].

        A = π(D/2)²
        """

        radius = self.entrance_pupil / 2

        return math.pi * radius**2

    # ------------------------------------------------------

    def signal_to_noise_estimate(
        self,
        object_flux,
        sky_flux,
    ):
        """
        Estimate the signal-to-noise ratio (SNR).

        Parameters
        ----------
        object_flux : float
            Object photon rate [electrons/sec]

        sky_flux : float
            Sky background rate [electrons/sec]

        Returns
        -------
        float
            Estimated SNR.

        Notes
        -----

                     Signal
        SNR = ------------------------
                  sqrt(S+B+D+RN²)

        S  = object electrons
        B  = sky electrons
        D  = dark current electrons
        RN = read noise
        """

        signal = object_flux * self.exposure_time

        background = sky_flux * self.exposure_time

        dark = self.dark_current * self.exposure_time

        total_noise = math.sqrt(
            signal
            + background
            + dark
            + self.read_noise**2
        )

        return signal / total_noise

    # ------------------------------------------------------

    def __str__(self):

        return (
            f"{self.exposure_time}s | "
            f"ISO {self.iso} | "
            f"f/{self.aperture} | "
            f"{self.focal_length} mm"
        )