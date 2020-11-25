# Imports
import os
from api import app_3D
from api.src.utils.d_target_to_map import TargetToMap

# Create the port
port = int(os.environ.get("PORT", 5000))


# Run the app
if __name__ == '__main__':
    # print(TargetToMap(51.319986, 5.077554).to_map())
    app_3D.run('0.0.0.0', port=port, debug=False, threaded=False)

